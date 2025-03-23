from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()

SYSTEM_PROMPT = """You are a strategy advisor for the board game Twilight Imperium 4th Edition.
Your purpose is to provide strategic advice, explain game mechanics, discuss faction strengths and weaknesses,
and help players improve their gameplay. Be concise and accurate about game rules and strategies.
Focus on:
- Faction selection and playstyles
- Strategic and tactical actions
- Political strategy
- Resource management
- Fleet composition
- Technology paths
- Objective completion strategies
- Diplomacy and negotiation tactics"""

def main():
    print("Twilight Imperium 4E Strategy Advisor")
    print("Type 'exit' to quit\n")
    
    # Keep track of conversation history
    conversation_history = []
    
    while True:
        # Get user input
        user_message = input("\nYour question: ")
        
        # Check for exit command
        if user_message.lower() in ["exit", "quit", "bye"]:
            print("Thanks for using the TI4 Strategy Advisor. Good luck conquering the galaxy!")
            break
        
        # Add user message to conversation history
        conversation_history.append({"role": "user", "content": user_message})
        
        try:
            # Create a streaming response
            with client.messages.stream(
                model="claude-3-5-sonnet-20240620",
                system=SYSTEM_PROMPT,
                messages=conversation_history,
                max_tokens=1000,
            ) as stream:
                # Print "Thinking..." initially
                print("\nThinking...", end="\r")
                
                # Process the stream
                assistant_response = ""
                print("\nResponse: ", end="")
                
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                    assistant_response += text
                
                print("\n")  # Add newline after response
        
            # Add assistant response to conversation history
            conversation_history.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()