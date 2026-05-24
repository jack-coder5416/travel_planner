import json
import os
import requests

from crewai.tools import BaseTool
from crewai import Agent, Task, LLM

from unstructured.partition.html import partition_html


llm_client = LLM(
    model = 'openrouter/openrouter/free',
    base_url = "https://openrouter.ai/api/v1",
    api_key = os.getenv('OPENAI_API_KEY')
)

class ScrapeWebsiteTool(BaseTool):

    name: str = "Scrape website content"

    description: str = (
        "Useful to scrape and summarize website content"
    )

    def _run(self, website: str) -> str:

        url = (
            f"https://chrome.browserless.io/content"
            f"?token={os.environ['BROWSERLESS_API_KEY']}"
        )

        payload = json.dumps({
            "url": website
        })

        headers = {
            'cache-control': 'no-cache',
            'content-type': 'application/json'
        }

        response = requests.post(
            url,
            headers=headers,
            data=payload
        )

        elements = partition_html(text=response.text)

        content = "\n\n".join(
            [str(el) for el in elements]
        )

        chunks = [
            content[i:i + 8000]
            for i in range(0, len(content), 8000)
        ]

        summaries = []

        for chunk in chunks:

            agent = Agent(
                role='Principal Researcher',

                goal=(
                    'Do amazing research and summaries '
                    'based on the content'
                ),

                backstory=(
                    "You're an expert researcher "
                    "working on website analysis."
                ),
                llm=llm_client,
                allow_delegation=False,
                verbose=False
            )

            task = Task(
                agent=agent,

                description=f"""
                Analyze and summarize the content below.

                Make sure to include the most relevant information.

                Return ONLY the summary.

                CONTENT:
                ----------------
                {chunk}
                """
            )

            summary = task.execute_sync()

            summaries.append(str(summary))

        return "\n\n".join(summaries)