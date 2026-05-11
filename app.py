import streamlit as st
import google.generativeai as genai

# Configure API
genai.configure(api_key="AIzaSyBI4uO3HH-M7nZiZL4rWTcjxi7HD8THWTk")

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Health Assistant")

st.title("🩺 AI Health Assistant")

st.write("Enter your symptoms below")

symptoms = st.text_area("Symptoms")

emergency_keywords = [
    "chest pain",
    "breathing problem",
    "unconscious",
    "heart attack",
    "severe bleeding"
]

if st.button("Analyze"):

    if any(word in symptoms.lower() for word in emergency_keywords):
        st.error("⚠ Emergency detected! Please contact a doctor immediately.")

    prompt = f"""
    User symptoms: {symptoms}

    Give:
    1. Possible illness
    2. Basic precautions
    3. Diet suggestions
    4. When to see a doctor

    Keep response simple.
    """

    response = model.generate_content(prompt)

    st.subheader("AI Analysis")
    st.write(response.text)

st.warning("This app does not replace professional medical advice.")