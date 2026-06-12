from crewai import Task
from agents.bio_analist import bio_analist

bio_analist_task=Task(
    description="",
    expected_output="",
    agent=bio_analist
)

