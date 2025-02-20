import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_product_description(details):
    prompt = f"Generate a creative, persuasive product description based on the following details:\n{details}\nDescription:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a marketing expert specialized in product descriptions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    details = input("Enter product details (features, target audience, etc.): ")
    description = generate_product_description(details)
    print("\nGenerated Product Description:\n", description)
