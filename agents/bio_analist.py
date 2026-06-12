from crewai import Agent
from config import settings

bio_analist=Agent(
    role="",
    backstory="",
    goal="",
    allow_delegation=True,
    verbose=True,
    llm=""
)