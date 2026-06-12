from crewai import Crew, Process
from agents.bio_transformer import bio_transformer
from agents.bio_analist import bio_analist
from agents.bio_validation import bio_specialist
from tasks.bio_transformer_task import bio_transformer_task
from tasks.bio_analist_task import bio_analist_task
from tasks.bio_specialist_task import bio_specialist_task

 class BioCrew(Crew):
    def BioCrew(self):