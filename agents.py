from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def qa_tester(self):
        return Agent(
            role="Admin Officer",
            backstory=dedent(f"""\
				You are an Admin Officer that specializes in  answering user questions"""),
            goal=dedent(f"""ensure that you respond to the client professionally with humour"""),

            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

