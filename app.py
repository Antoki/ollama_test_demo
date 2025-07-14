import streamlit as st
from ollama import chat, ChatResponse

import misc

# List of available models (edit as needed)
OLLAMA_MODELS = [
    "llama3.2",
    "gemma3",
    "qwen3",
    "mistral"
]

st.title("Ollama LLM Demo")

prompt = st.text_area("Enter your prompt:", height=120)
model = st.selectbox("Select a model:", OLLAMA_MODELS)
run = st.button("Submit")

output = ""

if run and prompt.strip():
    with st.spinner("Downloading model if not already..."):
        misc.download_model_if_not_exists(model)
    with st.spinner("Running model..."):
        try:
            response: ChatResponse = chat(
                model='llama3.2',
                messages=[{'role': 'user', 'content': prompt}],
            )
            output = response.message.content
        except Exception as e:
            output = f"Error: {str(e)}"
    st.subheader("Output:")
    st.text_area("Model Output", value=output, height=200)
elif run:
    st.warning("Please enter a prompt.")
