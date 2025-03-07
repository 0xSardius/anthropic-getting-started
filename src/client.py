from dotenv import load_dotenv
import os
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic()

our_first_message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "gm! Please tell me a joke about a curly goose"}
    ]
)

def main():
    
    print(our_first_message.content[0].text)
if __name__ == "__main__":
    main() 