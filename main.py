from gpt4all import GPT4All
import os
from flask_cors import CORS
import traceback
from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response



os.environ["GPT4ALL_NO_CUDA"] = "1"

    

model_path = r"C:\Users\neels_xc\AILocal\mythomax-l2-13b.Q4_K_M.gguf"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Cannot find model file at: {model_path}")



model = GPT4All(model_path)
app = Flask(__name__, template_folder="temp", static_folder="static")
chat_history = []


CORS(app, resources={r"/chat": {"origins": ["http://127.0.0.1:5500"]}})




max_tokens = 150
temp = 0.7
top_k = 40
top_p = 0.9
repeat_penalty = 1.1




def build_prompt(history):
    prompt = "You are OctoBot, a friendly and helpful assistant. Keep replies short and natural."
    for turn in history[:-1]:
        prompt += f"\nYou: {turn['user']}\nOctoBot: {turn['bot']}"
    prompt += f"\nYou: {history[-1]['user']}\nOctoBot:"
    return prompt  


@app.route("/")
def home():
    font = request.cookies.get("font", "Segoe UI")
    theme = request.cookies.get("theme", "Ultraviolet")
    return render_template("index.html", font=font, theme=theme)

@app.route("/settings", methods=["GET"])
def settings():
    font = request.cookies.get("font", "Segoe UI")
    theme = request.cookies.get("theme", "Ultraviolet")
    return render_template("settings.html", font=font, theme=theme)

@app.route("/saveSettings", methods=["POST"])
def saveSettings():
    font = request.form.get("font", "Segoe UI")
    theme = request.form.get("theme", "Ultraviolet")


    response = make_response(redirect(url_for("settings")))

    response.set_cookie("font", font) 
    response.set_cookie("theme", theme) 

    return response



   
@app.route("/chat", methods=["GET"])
def chat():
    font = request.cookies.get("font", "Segoe UI")
    theme=request.cookies.get("theme", "Ultraviolet")
    return render_template("octobot.html", font=font, theme=theme)



@app.route("/chat", methods=["POST"])
def chatUi():
    font = request.cookies.get("font", "Segoe UI")
    theme = request.cookies.get("theme", "Ultraviolet")
    userInput = request.json.get("message", "").strip()

    try:
        chat_history.append({'user': userInput, 'bot': ""})
        prompt = build_prompt(chat_history)

        print("=== Prompt Sent to Model ===")
        print(prompt)

        with model.chat_session():
            response = model.generate(
                prompt,
                max_tokens=max_tokens,
                temp=temp,
                top_k=top_k,
                top_p=top_p,
                repeat_penalty=repeat_penalty
            )
     
        print("Pure Response:")
        print(response)

        reply = response.strip()
        chat_history[-1]['bot'] = reply
        return jsonify({"response": reply})       



    except Exception as e:
        print("Error")
        traceback.print_exc()
        return jsonify({"response": f"Error occurred: {str(e)}"})
    


if __name__ == "__main__":
    app.run(debug=True, port=5500)
    