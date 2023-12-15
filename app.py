# Q&A Chatbot
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage,AIMessage
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os

## Function to load OpenAI model and get respones

def get_openai_response(question):
    llm_chat=ChatOpenAI(openai_api_key= os.getenv("OPENAI_API_KEY"),model_name="gpt-3.5-turbo",temperature=0.5)
    # llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),model_name="gpt-3.5-turbo",temperature=0.5)
    response=llm_chat([
    SystemMessage(content="you are a comedian AI Assistant"),
    HumanMessage(content=question),
    ])
    return response.content

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
