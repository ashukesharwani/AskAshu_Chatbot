# AskAshu_Chatbot

AskAshu_Chatbot is an interactive AI chatbot built using Streamlit and LangChain, powered by Hugging Face models. It allows users to chat with an LLM (Large Language Model) in a simple web interface.

Link APP :- https://askashuchatbot.streamlit.app

## Features

- Chat with an AI assistant using natural language
- Powered by Hugging Face's Gemma model
- Remembers chat history during the session
- Easy to run locally

## Setup

1. **Clone the repository**  
   Download or clone this project to your local machine.

2. **Install dependencies**  
   Run the following command to install required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Hugging Face API token**  
   - Copy `.evn_sample` to `.env`  
   - Replace `"API_KEY"` with your Hugging Face API token in `.env`:
     ```
     HF_TOKEN="your_huggingface_api_token"
     ```

## Usage

Start the chatbot using Streamlit:

```sh
streamlit run AskAshuChatbot.py
```

Open the provided local URL in your browser to interact with the chatbot.

## File Structure

- `AskAshuChatbot.py` — Main Streamlit app
- `.env` — Environment variables (your Hugging Face token)
- `.evn_sample` — Sample environment file
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation
