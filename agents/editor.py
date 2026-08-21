import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from prompts.editor_prompt import EDITOR_SYSTEM_PROMPT

load_dotenv()


class EditorAgent:

    def __init__(self):
        self.llm = ChatOpenAI(
            model="openrouter/free",
            temperature=0.3,
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def edit(self, draft: str) -> str:

        messages = [
            ("system", EDITOR_SYSTEM_PROMPT),
            (
                "human",
                f"""
Here is the draft created by the Writer Agent:

--- BEGIN DRAFT ---

{draft}

--- END DRAFT ---

Review and improve this draft.
"""
            )
        ]

        response = self.llm.invoke(messages)

        return response.content