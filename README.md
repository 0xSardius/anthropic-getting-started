# Anthropic Claude API - Getting Started

This project demonstrates how to use the Anthropic Claude API to build AI-powered applications.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   ```
   pip install -e .
   ```
5. Create a `.env` file with your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Project Structure

- `src/` - Main source code directory
  - `client.py` - Anthropic API client setup
  - `examples/` - Example use cases
    - `chat.py` - Basic chat example
    - `streaming.py` - Streaming response example
    - `function_calling.py` - Function calling example
- `scripts/` - Utility scripts
- `tests/` - Test cases

## Usage

Run examples:

```
python -m src.examples.chat
python -m src.examples.streaming
python -m src.examples.function_calling
```

## License

MIT
