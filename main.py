from flask import Flask, request, jsonify
from gpt4all import GPT4All
import os
from flask_cors import CORS


model_path = r"C:\Users\neels_xc\AILocal\mythomax-l2-13b.Q4_K_M.gguf"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Cannot find model file at: {model_path}")



model = GPT4All(model_path)
app = Flask(__name__)
chat_history = []

app = Flask(__name__)
CORS(app)




max_tokens = 60 
temp = 0.7
top_k = 40
top_p = 0.9
repeat_penalty = 1.1




def build_prompt(history):
    prompt = "You are OctoBot, a friendly and helpful assistant. Keep replies short and natural."
    for turn in history:
        prompt += f"\nYou: {turn['user']}\nOctoBot: {turn['bot']}"
    prompt += f"\nYou: {history[-1]['user']}\nOctoBot:"
    return prompt




@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()

    if user_input.lower() == "$endconvo":
        return jsonify({"response": "This conversation has been closed."})

    try:
        chat_history.append({'user': user_input, 'bot': ""})
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

        print("=== Raw Response ===")
        print(response)

        reply = response.strip()
        chat_history[-1]['bot'] = reply
        return jsonify({"response": reply})

    except Exception as e:
        print("=== Error ===")
        print(e)
        return jsonify({"response": f"Error occurred: {str(e)}"})



if __name__ == "__main__":
    app.run(debug=True)
    