import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API Key not found. Please add it in .env file")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-flash-latest")

# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="AI Sales Engineer Agent", layout="wide")

st.title("🤖 AI Sales Engineer Agent")
st.write("Analyze client transcript and generate insights + architecture")

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.success("Using Gemini Model")

# -----------------------------
# Input
# -----------------------------
transcript = st.text_area("📄 Paste Client Discovery Call Transcript", height=200)

# -----------------------------
# Prompt Template
# -----------------------------
def generate_response(text):
    prompt = f"""
    You are an AI Sales Engineer.

    Analyze the following transcript and extract:

    1. Pain Points
    2. Current Tech Stack (if mentioned)
    3. Desired Outcome
    4. Recommended Solution Architecture (very important)

    Give output in this format:

    Pain Points:
    - ...

    Tech Stack:
    - ...

    Desired Outcome:
    - ...

    Solution Architecture:
    - Frontend:
    - Backend:
    - LLM:
    - Database:
    - Integrations:
    - scalability:

    Transcript:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text

# -----------------------------
# Button Action
# -----------------------------
if st.button("🚀 Generate Insights"):

    if transcript.strip() == "":
        st.warning("⚠️ Please enter transcript")
    else:
        with st.spinner("Generating insights..."):
            result = generate_response(transcript)

        st.success("✅ Analysis Complete")

        # Display output
        st.markdown("### 📊 Results")
        st.write(result)