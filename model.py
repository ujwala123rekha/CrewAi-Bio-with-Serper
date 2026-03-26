from crewai import LLM

def get_llm():
    return LLM(
        model="ollama/gemma3:4b",
        base_url="http://localhost:11434"
    )