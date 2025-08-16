from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")  # Replace with your LLM initialization

st.title("Q&A AI Assistant")
st.header("Ask me anything")

# Input field for the question
question = st.text_input("Enter your question")

def chat_llm(question):
    # Define the message template
    message = [
        ("system", "You are an AI assistant that helps users with their questions."),
        ("human", f"{question}")
    ]
    
    # Initialize the output parser
    output_parser = StrOutputParser()
    
    # Create the chat prompt
    chat = ChatPromptTemplate.from_messages(message)
    
    # Create the chain
    chain = chat | llm | output_parser
    
    # Run the chain
    response = chain.invoke({"question": question})
    
    return response

# Button to submit the question

submit = st.button("Ask")
if submit:
    if question:
        response = chat_llm(question)
        st.write(response)