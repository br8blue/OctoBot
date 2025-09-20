import os
from openai import OpenAI


with open('.env', 'r') as f:
    os.environ["OPENAI_API_KEY"] = f.read().strip()


client = OpenAI()

def octobotResponse(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "$endconvo":
            break
        response = octobotResponse(user_input)
        print("OctoBot: " + response)
