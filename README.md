# AutoGen Agents

A Python project that demonstrates the use of Microsoft's AutoGen framework with multiple LLM providers (Gemini and OpenAI).

## Features

- Support for both Google's Gemini and OpenAI's GPT models
- Easy provider switching through environment variables
- Code execution capabilities
- Configurable agent settings

## Setup

1. Clone the repository:
```bash
git clone https://github.com/vikas434/autogen_agents.git
cd autogen_agents
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up your environment variables in `.env`:
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
LLM_PROVIDER=gemini  # or "openai"
```

## Usage

Run the main script:
```bash
python main.py
```

### Example Output

Here's an example of the agent implementing a bubble sort algorithm:

```python
user (to assistant):
Sort the array with Bubble Sort: [8, 1, 5, 2, 3, 21, 13, 10, 15, 17, 12, 11, 14, 16, 18, 19, 20]

assistant (to user):
# filename: bubble_sort.py
def bubble_sort(l):
    """
    Sorts the given list 'l' in ascending order using the Bubble Sort algorithm.

    Args:
        l (list): A list of integers to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(l)
    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

print(bubble_sort([8, 1, 5, 2, 3, 21, 13, 10, 15, 17, 12, 11, 14, 16, 18, 19, 20]))

Output:
[1, 2, 3, 5, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
```

## Configuration

- Default provider is Gemini
- To switch providers, modify `LLM_PROVIDER` in `.env`
- Supports code execution in the `coding` directory
- Configurable agent parameters in `create_agents()`

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`
- Valid API keys for chosen providers 