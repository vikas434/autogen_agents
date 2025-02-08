# AutoGen Chat API

A FastAPI-based REST API that provides an interface to interact with AutoGen's AI agents using Google's Gemini model.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```
5. Edit `.env` and add your Google API key

## Running the API

Run the server with:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Welcome message
- `POST /chat` - Send a message to the AI assistant
  - Request body:
    ```json
    {
        "message": "Your message here"
    }
    ```
  - Response:
    ```json
    {
        "response": "AI assistant's response"
    }
    ```

## Documentation

API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc` 