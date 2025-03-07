"""
Function calling example using the Anthropic Claude API.
This example demonstrates how to use Claude's function calling capabilities.
"""

import sys
import os
import json

# Add the parent directory to the path so we can import the client module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import client

# Define a tool for weather information
weather_tool = {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g., San Francisco, CA"
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "The unit of temperature to use"
            }
        },
        "required": ["location"]
    }
}

def get_current_weather(location, unit="fahrenheit"):
    """
    Mock function to simulate getting weather data.
    In a real application, this would call a weather API.
    """
    # This is mock data - in a real app, you would call a weather API
    weather_data = {
        "location": location,
        "temperature": 72 if unit == "fahrenheit" else 22,
        "unit": unit,
        "forecast": ["sunny", "windy"],
        "humidity": 45
    }
    
    return weather_data

def function_calling_example():
    """
    Demonstrates Claude's function calling capabilities.
    """
    message = "What's the weather like in San Francisco?"
    
    print(f"Sending message to Claude: '{message}'")
    
    # First, get Claude's response with tool use
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": message}
        ],
        tools=[weather_tool]
    )
    
    # Check if Claude wants to call a function
    tool_calls = []
    for content in response.content:
        if content.type == "tool_use":
            print(f"\nClaude wants to use tool: {content.name}")
            print(f"With parameters: {content.input}")
            
            # Parse the function parameters
            params = content.input
            
            # Call our function with the parameters Claude provided
            if content.name == "get_current_weather":
                result = get_current_weather(
                    location=params["location"],
                    unit=params.get("unit", "fahrenheit")
                )
                
                # Add the tool call and result to our list
                tool_calls.append({
                    "id": content.id,
                    "name": content.name,
                    "input": params,
                    "output": result
                })
    
    # If Claude made tool calls, send the results back
    if tool_calls:
        print("\nSending tool results back to Claude...")
        
        # Create a new message with the tool results
        final_response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": message},
                {
                    "role": "assistant",
                    "content": [
                        {"type": "tool_use", "id": tool_calls[0]["id"], "name": tool_calls[0]["name"], "input": tool_calls[0]["input"]}
                    ]
                },
                {
                    "role": "user", 
                    "content": [
                        {"type": "tool_result", "tool_use_id": tool_calls[0]["id"], "result": json.dumps(tool_calls[0]["output"])}
                    ]
                }
            ]
        )
        
        # Print Claude's final response
        print("\nClaude's final response:")
        for content in final_response.content:
            if content.type == "text":
                print(content.text)
    
    else:
        # If no tool calls were made, just print Claude's response
        print("\nClaude's response:")
        for content in response.content:
            if content.type == "text":
                print(content.text)

if __name__ == "__main__":
    function_calling_example() 