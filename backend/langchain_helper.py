# backend/langchain_helper.py
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
llm = ChatOpenAI(
    temperature=0.5,
    model_name="llama3-70b-8192",
    openai_api_key=api_key,
    openai_api_base="https://api.groq.com/openai/v1"
)
question_prompt = ChatPromptTemplate.from_template("""
You are an expert question generator. Based on the context provided below, generate 7 thoughtful, academic-style questions.
CONTEXT:
{context}
QUESTIONS:
""")
question_chain = LLMChain(llm=llm, prompt=question_prompt)
