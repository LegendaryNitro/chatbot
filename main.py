import json
import os
import sys
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from langchain_community.tools import DuckDuckGoSearchRun
import requests
import PyPDF2

current_dir = os.getcwd()
file_path = os.path.join(current_dir, '../Questions.pdf')

with open(file_path, 'rb') as file:
    pdf = PyPDF2.PdfReader(file)
    questions = []
    for page in range(len(pdf.pages)):
        page_obj = pdf.pages[page]
        questions.append(page_obj.extract_text())

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_ORGANIZATION"] = os.getenv("OPENAI_ORGANIZATION_ID")

class CustomCrew:
    def __init__(self, question):
        self.question = question

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        qa_tester = agents.qa_tester()

        create_homepage = tasks.answer_question(
             qa_tester,
             self.question,
            questions[0]# Use the first question from the PDF
        )

        crew = Crew(
            agents=[
                qa_tester,
               
                    ],
            tasks=[
                    create_homepage,

                   ],
            verbose=True,
            Process=Process.sequential,
        )

        result = crew.kickoff()
        return result