import streamlit as st
import os
from  dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers  import  StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_community.llms import Ollama 
## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="SIMPLE Q & A CHATBOT WITH OLLAMA"


## prompt template

prompt=ChatPromptTemplate.from_messages([("system","You are a helpful asistant . Please respond to the users queries"),("user","Question:{question}")])

def generate_response(question,engine,temperature,max_tokens):

    llm=Ollama(model=engine)
    outputparser=StrOutputParser()
    chain=prompt|llm|outputparser
    answer=chain.invoke({"question":question})
    return answer

##Title of the app

st.title("Enhanced Q&A chatbot with Groq")

## sidebar for settings

st.sidebar.title("settings")


##select the open source models
engine=st.sidebar.selectbox("Select Open Source model",["mistral:7b","phi3"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max_tokens",min_value=50,max_value=300,value=50)

## main interface for the user input

st.write("Go ahead and  ask any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")

