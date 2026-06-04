import streamlit as st
from groq import Groq

api_key = "YOUR_GROQ_API_KEY"
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


        with st.spinner("Generating Response..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": situation
                    }
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )

            output = response.choices[0].message.content

        st.success("Response Generated Successfully")

    st.text_area(
        "AI Response",
        output,
        height=300
    )