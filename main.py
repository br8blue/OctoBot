from gpt4all import GPT4All
import os


model_path = "C:/Users/neels_xc/OneDrive/Desktop/GPTLocal"
model_file = "nomic-ggml-gpt4all-falcon-Q4_K.gguf"
full_path = os.path.join(model_path, model_file)

if not os.path.exists(full_path):
    raise FileNotFoundError(f"Cannot find model file at: {full_path}")


model = GPT4All(model_file, model_path=model_path)


print("Hello there! My name is Octobot. How may I help you?\nNote: if at any point you'd like to end the conversation, please type $endconvo\n")


while True:
    user_input = input("You: ")

    if user_input.strip() == "$endconvo":
        print("OctoBot: Conversation ended. See you next time!")
        break

    try:

        response = model.chat_completion([
            {"role": "user", "content": user_input}
        ])
        print("\nOctoBot:", response, "\n")
    except Exception as e:
        print("OctoBot: Error occurred:", e)