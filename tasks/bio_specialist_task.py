from crewai import Task
from agents.bio_validation import bio_specialist


bio_specialist_task=Task(
    description = "",
    expected_output="",
    agent=bio_specialist
)