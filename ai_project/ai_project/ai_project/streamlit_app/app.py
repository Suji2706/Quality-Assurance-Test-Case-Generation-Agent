import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv(dotenv_path=os.path.join("..", "..", "env_site", ".env"))
print("Loaded GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

# Get Groq API key from .env
groq_api_key = os.getenv("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")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Streamlit page setup
st.set_page_config(page_title="🧠 AI Test Case Generator", layout="centered")
st.title("🧠 AI Test Case Generator")

# Text input
requirement = st.text_area("Enter your software requirement here:")

# Button to generate test cases
if st.button("Generate Test Cases"):
    if not requirement.strip():
        st.error("Please enter a requirement first.")
    else:
        with st.spinner("Generating test cases..."):
            try:
                # Use Groq’s LLaMA model to generate QA test cases
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": "You are a skilled QA engineer who writes clear and detailed test cases."},
                        {"role": "user", "content": f"Generate detailed software test cases for: {requirement}"}
                    ],
                    temperature=0.5,
                    max_tokens=800
                )

                # Extract the model output
                testcases = response.choices[0].message.content
                st.subheader("✅ Generated Test Cases")
                st.code(testcases)

            except Exception as e:
                st.error(f"Error generating test cases: {e}")
