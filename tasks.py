from crewai import Task
from textwrap import dedent

class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
                
        

    def answer_question(self, agent, question, source):

        return Task(
        description=dedent(
            f"""\
              your task is to use this {source} and answer the questions given by the user, here is the question {question}.
              if the question asked by the user doesn't apply provide a response that is polite implimenting that the question asked cannot be answered.

        {self.__tip_section()}
          """
        ),
        expected_output=dedent(f"""\
       a text response, tabulate if need be',
                               """),
        agent=agent,

    )

   