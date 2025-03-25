from anthropic import Anthropic
from dotenv import load_dotenv
import base64

load_dotenv()

client = Anthropic()

# opens the image file in "read binary" mode
with open("src/examples/images/uh_oh.png", "rb") as image_file:

    #reads the contents of the image as a bytes object
    binary_data = image_file.read() 

    #encodes the binary data using Base64 encoding
    base_64_encoded_data = base64.b64encode(binary_data) 

    #decodes base_64_encoded_data from bytes to a string
    base64_string = base_64_encoded_data.decode('utf-8')

messages = [
    {
        "role": "user",
        "content": [{
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_string
            },
        },
        {
            "type": "text",
            "text": "What could the person have done to prevent this?"
        }]
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)









# messages = [
#      {
#         "role": "user",
#         "content": [
#             {"type": "text", "text": "tell me a joke"},
#         ]
#     }
# ]

# response = client.messages.create(
#     messages=messages,
#     model="claude-3-5-sonnet-20240620",
#     max_tokens=200
# )
# print(response.content[0].text)