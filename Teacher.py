from crewai import Agent
from llm.model import get_llm


def create_teacher():
    return Agent(
        role="Teacher",
        goal="Explain topics in a simple way",
        backstory="Expert at simplifying complex ideas",
        llm=get_llm(),
        verbose=False
    )