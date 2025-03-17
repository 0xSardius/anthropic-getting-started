from dotenv import load_dotenv
from anthropic import Anthropic
import time

load_dotenv()

client = Anthropic()

# truncated_response = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=10,
#     messages=[
#         {"role": "user", "content": "Write me a poem"}
#     ]
# )
# print(truncated_response.content[0].text)
# print(truncated_response.stop_reason)


# longer_poem_response = client.messages.create(
#     model="claude-3-haiku-20240307",
#     max_tokens=500,
#     messages=[
#         {"role": "user", "content": "Write me a poem about lemongrab from the show Adventure Time"}
#     ]
# )
# print(longer_poem_response.content[0].text)
# print(longer_poem_response.stop_reason)

# def compare_num_tokens_speed():
#     token_counts = [100, 1000, 4096]
#     task = """
#         Create a long, detailed dialogue that is at least 5000 words between two characters discussing the impact of social media on society.
#         The characters should have differing opinions and engage in a respectful thorough debate.
#     """

#     for num_tokens in token_counts:
#         start_time = time.time()

#         response = client.messages.create(
#             model="claude-3-haiku-20240307",
#             max_tokens=num_tokens,
#             messages=[
#                 {"role": "user", "content": task}
#             ]
#         )

#         end_time = time.time()
#         duration = end_time - start_time
#         print(f"Tokens: {num_tokens}, Duration: {duration:.2f} seconds")

# compare_num_tokens_speed()

# def json_creator():
#     response = client.messages.create(
#         model="claude-3-haiku-20240307",
#         max_tokens=4096,
#         messages=[
#             {"role": "user", "content": "Create a JSON object with the following fields: name, age, email"}
#         ],
#         stop_sequences=["}"]
#     )
#     print(response.content[0].text)

# def generate_random_letters_3_times():
#     for i in range(3):
#         response = client.messages.create(
#             model="claude-3-haiku-20240307",
#             max_tokens=500,
#             messages=[{"role": "user", "content": "generate a poem"}],
#             stop_sequences=["b", "c"]
#         )
#         print(f"Response {i+1} stopped because {response.stop_reason}.  The stop sequence was {response.stop_sequence}")

# generate_random_letters_3_times()

# def demonstrate_temperature():
#     temperatures = [0, 1]
#     for temperature in temperatures:
#         print(f"Prompting Claude three times with temperature {temperature}")
#         print("-" * 40)
#         for i in range(3):
#             response = client.messages.create(
#                 model="claude-3-haiku-20240307",
#                 max_tokens=100,
#                 messages=[{"role": "user", "content": "Come up with some cool names for Yssaril Tribe themed factions in Twilight Imperium"}],
#                 temperature=temperature
#             )
#             print(f"Response {i+1}: {response.content[0].text}")

# demonstrate_temperature()

# Exercise

def generate_questions(topic, num_questions):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        system="You are a helpful assistant that generates thought provoking questions about a given topic.",
        messages=[
            {"role": "user", "content": f"Generate {num_questions} questions about {topic}"}
        ]
    )
    return response.content[0].text

def respond_to_questions(questions):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        system="You are a helpful assistant that answers questions about a given topic.",
        messages=[
            {"role": "user", "content": f"Answer the following questions: {questions}"}
        ]
    )
    return response.content[0].text

ai_questions = generate_questions("Intersection of AI and web3", 5)

print(ai_questions)

ai_answers = respond_to_questions(ai_questions)

print(ai_answers)

