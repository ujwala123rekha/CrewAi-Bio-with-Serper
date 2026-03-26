from crewai import Agent
from llm.model import get_llm


def create_reviewer():
    return Agent(
        role="Reviewer",
        goal="Improve clarity and correctness",
        backstory="Strict editor ensuring high-quality output",
        llm=get_llm(),
        verbose=False
    )