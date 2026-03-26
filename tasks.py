from crewai import Task

RESEARCH_TEMPLATE = """
You are an expert data extractor.

Use ONLY the information below.
Do NOT guess.
Do NOT add extra information.

If any information is missing, write: Not Available

Extract and organize the information in this EXACT format:

Name:
Date of Birth:
Place of Birth:
Nationality:
Profession:

Career / Fields:
- 

Current Status:
- 

Awards / Achievements:
- 

Important Notes:
- 

Information:
{context}

Topic: {topic}
"""

EXPLAIN_TEMPLATE = """
You are a teacher.

Using ONLY the research above,
explain the topic simply.

Rules:
- Do NOT add new facts
- Do NOT guess
- Keep language simple

Topic: {topic}
"""


REVIEW_TEMPLATE = """
You are a strict reviewer.

Task:
- Remove wrong information
- Improve clarity
- Fix grammar
- Remove useless text

Rules:
- Do NOT apologize
- Do NOT talk about AI
- Output ONLY final answer
"""


def create_tasks(topic, context, researcher, teacher, reviewer):

    # Research (uses real data)
    task1 = Task(
        description=RESEARCH_TEMPLATE.format(
            topic=topic,
            context=context
        ),
        agent=researcher,
        expected_output="Factual research notes"
    )

    # Explain
    task2 = Task(
        description=EXPLAIN_TEMPLATE.format(topic=topic),
        agent=teacher,
        expected_output="Simple explanation"
    )

    # Review
    task3 = Task(
        description=REVIEW_TEMPLATE,
        agent=reviewer,
        expected_output="Final polished answer"
    )

    return [task1, task2, task3]