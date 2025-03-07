"""
Basic chat example using the Anthropic Claude API.
This example demonstrates how to send a simple message to Claude and get a response.
"""

import sys
import os

# Add the parent directory to the path so we can import the client module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import client

def simple_chat():
    """
    Demonstrates a simple chat with Claude.
    """
    message = "Hello Claude! Tell me about yourself in 2-3 sentences."
    
    print(f"Sending message to Claude: '{message}'")
    print("\nResponse from Claude:")
    
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=300,
        messages=[
            {"role": "user", "content": message}
        ]
    )
    
    print(response.content[0].text)
    
    return response

if __name__ == "__main__":
    simple_chat() 