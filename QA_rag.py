import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
#os.environ["LANGCHAIN_TRACING_V2"]="true"
#os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

##prompt template
prompt=ChatPromptTemplate.from_messages(
    [("system","You are a helpful assistant. Please respond to the question asked"),("user","{input}")])

parser=StrOutputParser()
llm=Ollama(model="gemma:2b")
chain=prompt|llm | parser

## streamlit app
st.title("Simple Q&A chatbot")
text_input=st.text_input("What question is in mind")
if text_input:
    st.write(chain.invoke({"input":text_input}))
