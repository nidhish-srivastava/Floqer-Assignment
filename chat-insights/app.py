# import streamlit as st
# import pandas as pd
# from langchain.document_loaders.csv_loader import CSVLoader
# from langchain.vectorstores import FAISS
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.prompts import PromptTemplate
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import LLMChain
# from dotenv import load_dotenv
# import openai
# import os

# load_dotenv()

# # Step 1: Set Up OpenAI API
# openai.api_key = os.getenv("sk-proj-uM3bGut32FNAnH2WILwOT3BlbkFJAP1KgOc03WMm6BuEX2H3")

# # Step 2: Define a Chat Interface
# def chat_interface():
#     st.title("ML Engineer Salary Insights Chat")
#     user_input = st.text_input("Enter your query")

#     if user_input:
#         response = generate_response(user_input)
#         st.text_area("Response", value=response, height=200)

# # Step 3: Retrieve Data
# @st.cache
# def load_salary_data():
#     return pd.read_csv("salaries.csv")

# data = load_salary_data()

# # Step 4: Set Up LLMChain & Prompts
# llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

# template = """
# You are an expert in analyzing salary data. Here is a relevant portion of the dataset of ML engineer salaries:
# {data}

# Based on this data, please provide insights for the following query:
# {query}
# """

# prompt = PromptTemplate(
#     input_variables=["data", "query"],
#     template=template
# )

# chain = LLMChain(llm=llm, prompt=prompt)

# # Step 5: Generate Responses
# def generate_response(query):
#     # Extract relevant data based on the query
#     relevant_data = extract_relevant_data(query)
#     relevant_data_str = relevant_data.to_string(index=False)
    
#     # Ensure the prompt stays within the size limits
#     if len(relevant_data_str) > 1000:
#         relevant_data_str = relevant_data_str[:1000] + "\n... (truncated)"

#     response = chain.run(data=relevant_data_str, query=query)
#     return response

# def extract_relevant_data(query):
#     # Implement a basic extraction logic based on keywords in the query
#     if "2022" in query:
#         return data[data['Year'] == 2022]
#     elif "2023" in query:
#         return data[data['Year'] == 2023]
#     elif "2020" in query:
#         return data[data['Year'] == 2020]
#     elif "2021" in query:
#         return data[data['Year'] == 2021]
#     elif "2024" in query:
#         return data[data['Year'] == 2024]
#     else:
#         # Default to showing summary of all years
#         return data

# # Step 6: Display Responses
# def main():
#     chat_interface()

# if __name__ == "__main__":
#     main()
import streamlit as st
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import openai
import os


load_dotenv()


openai.api_key = os.getenv("sk-proj-uM3bGut32FNAnH2WILwOT3BlbkFJAP1KgOc03WMm6BuEX2H3")


def chat_interface():
    st.title("Job Salary Insights Chat")
    user_input = st.text_input("Enter your query")

    if user_input:
        response = generate_response(user_input)
        st.text_area("Response", value=response, height=200)


@st.cache
def load_salary_data():
    return pd.read_csv("salaries.csv")

data = load_salary_data()


llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

template = """
You are an expert in analyzing salary data. Here is a relevant portion of the dataset of job salaries:
{data}

Based on this data, please provide insights for the following query:
{query}
"""

prompt = PromptTemplate(
    input_variables=["data", "query"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)


def generate_response(query):
    
    relevant_data = extract_relevant_data(query)
    relevant_data_str = relevant_data.to_string(index=False)
    
    # Ensure the prompt stays within the size limits
    if len(relevant_data_str) > 1000:
        relevant_data_str = relevant_data_str[:1000] + "\n... (truncated)"

    response = chain.run(data=relevant_data_str, query=query)
    return response

def extract_relevant_data(query):
    # Implement a basic extraction logic based on keywords in the query
    if "2022" in query:
        return data[data['Year'] == 2022]
    elif "2023" in query:
        return data[data['Year'] == 2023]
    elif "2020" in query:
        return data[data['Year'] == 2020]
    elif "2021" in query:
        return data[data['Year'] == 2021]
    elif "2024" in query:
        return data[data['Year'] == 2024]
    else:
        
        return data


def main():
    chat_interface()

if __name__ == "__main__":
    main()
