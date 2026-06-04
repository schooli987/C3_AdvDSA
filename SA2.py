import streamlit as st
from groq import Groq

api_key = "Your_API_Key_Here"
client = Groq(api_key=api_key)

st.set_page_config(
    page_title="AI Personality Generator",
    page_icon="🎭"
)

st.title("🎭 AI Personality Generator")

st.write("Generate AI responses with different personalities")

situation = st.text_area(
    "Enter a Situation",
    placeholder="I have an exam tomorrow and I feel nervous."
)

personality = st.selectbox(
    "Choose Personality",
    [
        "Motivational Coach",
        "Funny Friend",
        "Strict Teacher",
        "Professional Mentor",
        "Scientist",
        "Philosopher"
    ]
)

tone = st.selectbox(
    "Choose Tone",
    [
        "Friendly",
        "Professional",
        "Funny",
        "Serious",
        "Motivational"
    ]
)

temperature = st.slider(
    "Creativity Level",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

max_tokens = st.slider(
    "Response Length",
    min_value=100,
    max_value=800,
    value=300,
    step=100
)

generate = st.button("Generate Response")

if generate:

    if situation.strip() == "":

        st.warning("Please enter a situation")

    else:

        system_prompt = f"""
        You are acting as a {personality}.

        Respond in a {tone} tone.

        Give meaningful and engaging responses.
        """

        st.success("System Prompt Created Successfully")

        st.text_area(
            "Generated System Prompt",
            system_prompt,
            height=200
        )