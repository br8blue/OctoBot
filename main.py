from gpt4all import GPT4All
import os
import flask

model_path = r"C:\Users\neels_xc\AILocal\mythomax-l2-13b.Q4_K_M.gguf"
model_file = "mythomax-l2-13b.Q4_K_M.gguf"
full_path = r"C:\Users\neels_xc\AILocal\mythomax-l2-13b.Q4_K_M.gguf"

model = GPT4All(r"C:\Users\neels_xc\AILocal\mythomax-l2-13b.Q4_K_M.gguf")




if not os.path.exists(full_path):
    raise FileNotFoundError(f"Cannot find model file at: {full_path}")



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
