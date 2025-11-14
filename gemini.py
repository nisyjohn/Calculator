import streamlit as st
import google.generativeai as genai
st.title("Welcome to the Genai app of Nisy")
user_input = st.text_input("Hey, Ask me anything about Genai")
genai.configure(api_key="AIzaSyDz838Td9zFQsUXWaSN466fPC8FqW__unE")
model = genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
        try:
                response=model.generate_content(user_input)
                st.write("Gemini", response.text)
        except Exception as e:
                st.error(f"An error occurred: {e}")