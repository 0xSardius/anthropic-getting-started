"""
Streaming example using the Anthropic Claude API.
This example demonstrates how to stream responses from Claude in real-time.
"""

import sys
import os

# Add the parent directory to the path so we can import the client module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import client

def streaming_chat():
    """
    Demonstrates streaming responses from Claude.
    """
    message = "Write a short poem about artificial intelligence."
    
    print(f"Sending message to Claude: '{message}'")
    print("\nStreaming response from Claude:")
    
    with client.messages.stream(
        model="claude-3-sonnet-20240229",
        max_tokens=300,
        messages=[
            {"role": "user", "content": message}
        ]
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        
        print("\n\nStream completed.")
        
        # You can also access the final message
        final_message = stream.get_final_message()
        print(f"\nFinal message ID: {final_message.id}")

if __name__ == "__main__":
    streaming_chat() 