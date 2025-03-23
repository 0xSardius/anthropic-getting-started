from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

with client.messages.stream(
    messages=[
        {
            "role": "user",
            "content": "Write me an essay about chivalry in the 14th century.",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=800,
    temperature=0,
) as stream:
    print("Streaming response:")
    print("==================")
    # Print the response as it comes in
    for text in stream.text_stream:
        print(text, end="", flush=True)
    print("\n\nStream completed.")

stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "Write me a 3 word sentence, without a preamble.  Just give me 3 words",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=100,
    temperature=0,
    stream=True,
)
for event in stream:
    if event.type == "content_block_delta":
        print(event.delta.text, flush=True, end="")


async def streaming_with_helpers():
    async with client.messages.stream(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Write me sonnet about orchids",
            }
        ],
        model="claude-3-opus-20240229",
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)

    final_message = await stream.get_final_message()
    print("\n\nSTREAMING IS DONE.  HERE IS THE FINAL ACCUMULATED MESSAGE: ")
    print(final_message.to_json())

await streaming_with_helpers()