from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

conversation = []

while True:
    
    print("\nInstructions:")
    print("- Type your message and press Enter to chat with Claude")
    print("- Type 'exit' to end the conversation")
    print("- Type 'clear' to reset the conversation history\n")
    user_input = input("Please enter a message to send to the chatbot: ").strip()

    # Only proceed if the user input is not empty
    if user_input:
        # Add the user message to conversation history
        conversation.append({"role": "user", "content": user_input})
        
        # Make the API call with the updated conversation
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            messages=conversation
        )
    else:
        print("Message cannot be empty. Please try again.")
    
    conversation.append({"role": "assistant", "content": response.content[0].text})

    print(f"Chatbot: {response.content[0].text}")

    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "clear":
     # Reset the conversation history
        conversation = []
        print("Conversation history cleared.")
        continue
    
    


