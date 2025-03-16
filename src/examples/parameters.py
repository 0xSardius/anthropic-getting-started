from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

truncated_response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=10,
    messages=[
        {"role": "user", "content": "Write me a poem"}
    ]
)
print(truncated_response.content[0].text)
print(truncated_response.stop_reason)


longer_poem_response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Write me a poem about lemongrab from the show Adventure Time"}
    ]
)
print(longer_poem_response.content[0].text)
print(longer_poem_response.stop_reason)
