from crewai import Agent
from llm.model import get_llm


def create_researcher():
    return Agent(
        role="Researcher",
        goal="Analyze and summarize given information",
        backstory="Expert at extracting facts from documents",
        llm=get_llm(),
        verbose=False
    )