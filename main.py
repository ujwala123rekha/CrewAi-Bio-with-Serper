from Agents.Researcher import create_researcher
from Agents.Teacher import create_teacher
from Agents.Reviewer import create_reviewer

from Tasks.tasks import create_tasks
from Crew.crew import create_crew

import requests
import os
from dotenv import load_dotenv

load_dotenv()


# -------------------------------
# Web Search (Manual RAG)
# -------------------------------
def web_search(query):
    api_key = os.getenv("SERPER_API_KEY")

    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "q": query,
        "num": 5
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()


# -------------------------------
# Extract Text from Results
# -------------------------------
def extract_text(results):
    texts = []

    if "organic" in results:
        for item in results["organic"]:
            title = item.get("title", "")
            snippet = item.get("snippet", "")
            texts.append(f"{title}: {snippet}")

    return "\n".join(texts)


# -------------------------------
# MAIN
# -------------------------------
def main():

    print("\n=== Multi-Agent AI System ===")
    print("Type 'exit' to quit\n")

    while True:

        user_query = input("Ask something: ")

        if user_query.lower() == "exit":
            print("Goodbye 👋")
            break

        print("\nThinking...\n")

        # Agents
        researcher = create_researcher()
        teacher = create_teacher()
        reviewer = create_reviewer()

        agents = [researcher, teacher, reviewer]

        # Manual RAG
        search_results = web_search(user_query)
        context = extract_text(search_results)

        # Tasks
        tasks = create_tasks(
            user_query,
            context,
            researcher,
            teacher,
            reviewer
        )

        # Crew
        crew = create_crew(agents, tasks)

        result = crew.kickoff()

        print("\n=== Answer ===\n")
        print(result)
        print("\n=================\n")


if __name__ == "__main__":
    main()