from gpt4all import GPT4All
import os



model_path = r"C:\Users\neels_xc\AILocal\mythomax-l2-13b.Q4_K_M.gguf"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Cannot find model file at: {model_path}")



model = GPT4All(model_path)



max_tokens = 60 
temp = 0.7
top_k = 40
top_p = 0.9
repeat_penalty = 1.1



chat_history = []



def build_prompt(history):
    prompt = "You are OctoBot, a friendly and helpful assistant. Keep replies short and natural."
    for turn in history:
        prompt += f"\nYou: {turn['user']}\nOctoBot: {turn['bot']}"
    prompt += f"\nYou: {history[-1]['user']}\nOctoBot:"
    return prompt



print("OctoBot: Hi, I'm OctoBot! How can I help you today?")



while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit", "$endconvo"]:
        print("OctoBot: This conversation has been closed.")
        break

    chat_history.append({'user': user_input, 'bot': ""})
    prompt = build_prompt(chat_history)

    with model.chat_session():
        response = model.generate(
            prompt,
            max_tokens=max_tokens,
            temp=temp,
            top_k=top_k,
            top_p=top_p,
            repeat_penalty=repeat_penalty
        )



    reply = response.strip()
    chat_history[-1]['bot'] = reply
    print(f"OctoBot: {reply}")