from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

try:
    book_text = open("src/books/frankenstein.txt", "r", encoding="utf-8").read()
except UnicodeDecodeError:
    # If UTF-8 fails, try another common encoding
    book_text = open("src/books/frankenstein.txt", "r", encoding="latin-1").read()


def translate(word, language) :
    response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": f"Translate {word} to {language}. Respond with a single word in english."
            }
        ]
    )

    return response.content[0].text

result = translate("beautiful", "japanese")

print(result)





