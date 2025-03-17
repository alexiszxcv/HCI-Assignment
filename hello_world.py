import openai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_hello_world():
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative writer."},
            {"role": "user", "content": "Write a unique and creative 'Hello World' message."}
        ],
        max_tokens=50
    )

    message = response.choices[0].message.content
    return message.strip()

if __name__ == "__main__":
    creative_message = generate_hello_world()
    print(creative_message)
