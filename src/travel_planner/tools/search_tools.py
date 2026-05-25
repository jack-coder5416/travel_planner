import os
import requests

from crewai.tools import BaseTool
import streamlit as st

class SearchInternetTool(BaseTool):

    name: str = "Search Internet"

    description: str = (
        "Useful for searching the internet "
        "about a topic"
    )

    def _run(self, query: str) -> str:

        url = "https://google.serper.dev/search"

        payload = {
            "q": query
        }

        headers = {
            "X-API-KEY": st.secrets["SERPER_API_KEY"],
            "Content-Type": "application/json"
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        data = response.json()

        results = []

        if "organic" in data:

            for item in data["organic"][:5]:

                results.append(
                    f"""
Title: {item.get('title')}

Link: {item.get('link')}

Snippet: {item.get('snippet')}
"""
                )

        return "\n\n".join(results)