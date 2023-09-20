import openai
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(openai_api_key="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")
dreamDescription = ""

dreamPromptTemplate = PromptTemplate(
    input_variables = ['dream_Description'],
    template = "Please interpret the following archetypal dream: {dream_Description}"
)

st.title("Your Free Dream Interpreter")
st.write("""
         Describe your dream!

         Tip 1: Include any feelings or thoughts you had in the dream
           Ex: I saw my Grandfather sitting at a bar. I was excited to see him and he was pleased to see me but not excited.
           Ex: An eagle flew up to me. He was there to rescue me.
         
         """)


dreamDescription = st.text_area(label='Enter Your Dream Here', value= 'In my dream ')
if st.button("Interpret my Dream!"):
    interpretationResponse = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= [
        {"role": "system", "content" : "You are an archetypal dream interpreter. First give a breif summary of what the dreamer's subconscious is expressing to the dream. Then list the different archetypes of the dream."},
        {"role": "user", "content" : "Please interpret the following archetypal dream: {dream_Description}"}
        ],
    )

st.write(["choices"][0]["message"]["content"])
