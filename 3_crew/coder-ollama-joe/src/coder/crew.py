from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM  # Add this import
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class Coder():
    """Coder crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def coder(self) -> Agent:
        ollama_llm = LLM(
            model="ollama/llama3.2:latest",
            base_url="http://localhost:11434"
        )
        return Agent(
            config=self.agents_config['coder'],
            llm=ollama_llm,
            verbose=True,
            # allow_code_execution=True,
            # code_execution_mode="safe",  
            # max_execution_time=30,
            # max_retry_limit=3
        )

    @task
    def coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Coder crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )