from dotenv import load_dotenv
from anthropic import Anthropic
import time

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

def compare_num_tokens_speed():
    token_counts = [100, 1000, 4096]
    task = """
        Create a long, detailed dialogue that is at least 5000 words between two characters discussing the impact of social media on society.
        The characters should have differing opinions and engage in a respectful thorough debate.
    """

    for num_tokens in token_counts:
        start_time = time.time()

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=num_tokens,
            messages=[
                {"role": "user", "content": task}
            ]
        )

        end_time = time.time()
        duration = end_time - start_time
        print(f"Tokens: {num_tokens}, Duration: {duration:.2f} seconds")

compare_num_tokens_speed()

def json_creator():
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": "Create a JSON object with the following fields: name, age, email"}
        ],
        stop_sequences=["}"]
    )
    print(response.content[0].text)
