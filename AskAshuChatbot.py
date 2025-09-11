"""_Ask Ashu_
This is the Chat bot created by me it work like a LLM
"""

import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# 1. Load environment variables
load_dotenv()

# This is for running in locally
# hf_token = os.getenv("HF_TOKEN")

# This is for Streamlit app
HF_TOKEN = os.getenv("HF_TOKEN") or st.secrets.get("HF_TOKEN")

# Set up the page title and initial instructions
st.title("Ask Ashu Chatbot")
st.info("Ask me anything! Type 'exit' to end the chat.")


# Initialize the LLM and chat model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=HF_TOKEN
)
model = ChatHuggingFace(llm=llm)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI agent.")
    ]

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.chat_history.append(HumanMessage(content=prompt))

    # Invoke the model and display the response
    with st.chat_message("assistant"): 
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.chat_history)
        st.markdown(response.content)
        # Add AI response to chat history
        st.session_state.chat_history.append(AIMessage(content=response.content))
    
       
# how to run
# stremlit run AskAshuChatbot.py