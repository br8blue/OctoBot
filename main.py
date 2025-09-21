from gpt4all import GPT4All
import os


model_path = "C:/Users/neels_xc/OneDrive/Desktop/GPTLocal"
model_file = "nomic-ai-gpt4all-falcon-Q4_K.gguf"
full_path = os.path.join(model_path, model_file)

if not os.path.exists(full_path):
    raise FileNotFoundError(f"Cannot find model file at: {full_path}")


model = GPT4All(model_name=model_file, model_path=model_path)


print("OctoBot: Hello there! My name is Octobot. How may I help you?")
print("Type $endconvo to exit.\n")


with model.chat_session():
    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "$endconvo":
            print("This conversation has been closed.")
            break

        try:
            response = model.generate(user_input)

            if isinstance(response, str):
                print("OctoBot:", response.strip())
            else:
                print("OctoBot: Unexpected response type:", type(response))

        except Exception as e:
            print("OctoBot: Error occurred:", e)
