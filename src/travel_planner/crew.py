from crewai import Crew, Task, Agent, Process, LLM
from crewai.project import CrewBase, agent, task, crew

from .tools.browser_tools import ScrapeWebsiteTool
from .tools.calculator_tools import CalculatorTool
from .tools.search_tools import SearchInternetTool

import os
from dotenv import load_dotenv

load_dotenv()

llm_client = LLM(
    model = 'openrouter/openrouter/free',
    base_url = "https://openrouter.ai/api/v1",
    api_key = os.getenv('OPENAI_API_KEY')
)

@CrewBase
class TravelPlannerCrew():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    search_tool = SearchInternetTool()
    browser_tool = ScrapeWebsiteTool()
    calculator_tool = CalculatorTool()

    @agent
    def city_selection_agent(self) -> Agent:

        return Agent(
            config = self.agents_config['city_selection_agent'],
            llm = llm_client,
            verbose = True,
            tools = [
                self.search_tool, 
                self.browser_tool
            ]
        )
    
    @agent
    def local_expert_agent(self) -> Agent:

        return Agent(
            config = self.agents_config['local_expert_agent'],
            llm = llm_client,
            verbose = True,
            tools = [
                self.search_tool, 
                self.browser_tool
            ]
        )
    
    @agent
    def travel_concierge_agent(self) -> Agent:

        return Agent(
            config = self.agents_config['travel_concierge_agent'],
            llm = llm_client,
            verbose = True,
            tools = [
                self.search_tool, 
                self.browser_tool,
                self.calculator_tool,
            ]
        )
    
    @task
    def city_selection_task(self) -> Task:
        return Task(
            config = self.tasks_config['city_selection_task'],
            agent = self.city_selection_agent(),
            verbose = True
        )

    @task
    def local_expert_task(self) -> Task:
        return Task(
            config = self.tasks_config['local_expert_task'],
            agent = self.local_expert_agent(),
            verbose = True
        ) 

    @task
    def travel_concierge_task(self)-> Task:
        return Task(
            config = self.tasks_config['travel_concierge_task'],
            agent = self.travel_concierge_agent(),
            verbose = True
        ) 
    
    @crew
    def crew(self)-> Crew:
        return Crew(
            tasks = self.tasks,
            agents = self.agents,
            process = Process.sequential
        )