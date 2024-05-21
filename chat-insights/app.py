

import streamlit as st
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import openai
import os


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_interface():
    st.title("Job Salary Insights Chat")
    user_input = st.text_input("Enter your query")

    if user_input:
        response = generate_response(user_input)
        st.text_area("Response", value=response, height=200)


@st.cache_data
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
        return data[data['work_year'] == 2022]
    elif "2023" in query:
        return data[data['work_year'] == 2023]
    elif "2020" in query:
        return data[data['work_year'] == 2020]
    elif "2021" in query:
        return data[data['work_year'] == 2021]
    elif "2024" in query:
        return data[data['work_year'] == 2024]
    else:
        
        return data


def main():
    chat_interface()

if __name__ == "__main__":
    main()
