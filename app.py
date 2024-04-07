import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = st.secrets["API_TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def main():
    # Page configuration
    st.set_page_config(
        page_title="Streamlit QA Chatbot",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-image: linear-gradient(#2e7bcf,#2e7bcf);
                color: white;
            }
            .block-container {
                padding-top: 5rem;
                padding-bottom: 5rem;
            }
            h1 {
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Sidebar
    with st.sidebar:
        st.image("assets/images/logo.png", width=100)  # Adjust path as necessary
        st.header("QA Chatbot")
        st.markdown("#### Enter Question and Context for the AI to generate an answer.")

    # Main chat interface
    st.title("Streamlit QA Chatbot")

    question = st.text_input("Question:")
    context = st.text_area("Context:", height=150)

    if st.button("Get Answer"):
        if question and context:
            payload = {"inputs": {"question": question, "context": context}}
            output = query(payload)
            if "answer" in output:
                st.write(f"Answer: {output['answer']}")
            else:
                st.write("Could not find an answer.")
        else:
            st.write("Please provide both a question and context.")


if __name__ == "__main__":
    main()
