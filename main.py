from gpt4all import GPT4All
import os
import flask

model_path = r"C:\Users\neels_xc\AILocal\mythomax-l2-13b.Q4_K_M.gguf"


if not os.path.exists(model_path):
    raise FileNotFoundError(f"Cannot find model file at: {model_path}")


model = GPT4All(model_path)


chat_history = []


def build_prompt(history):
    prompt = "You are OctoBot, a helpful assistant. Keep replies short and natural."

    for turn in history:
        prompt += f"You: {turn['user']}\nOctoBot: {turn['bot']}\n"
    prompt += f"You: {history[-1]['user']}\nOctoBot:"
    return prompt


print("OctoBot: Hello there! My name is Octobot. How may I help you?")
print("If at any point you would like to end the conversation, type $endconvo.\n")

with model.chat_session():
    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "$endconvo":
            print("This conversation has been closed.")
            break

        try:
            if not chat_history:
                chat_history.append({'user': user_input, 'bot': ""})
            else:
                chat_history[-1]['bot'] = response.strip()
                chat_history.append({'user': user_input, 'bot': ""})

            prompt = build_prompt(chat_history)


            response = model.generate(
                prompt,
                max_tokens=30, 
                temp=0.7,
                top_k=40,
                top_p=0.9,
                repeat_penalty=1.1
)


            print("OctoBot:", response.strip())

        except Exception as e:
            print("Error occurred:", e)