import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from prompts.writer_prompt import WRITER_SYSTEM_PROMPT

load_dotenv()


class WriterAgent:

    def __init__(self):
        self.llm = ChatOpenAI(
            model="openrouter/free",
            temperature=0.7,
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

    def write(self, topic: str) -> str:

        messages = [
            ("system", WRITER_SYSTEM_PROMPT),
            ("human", topic)
        ]

        response = self.llm.invoke(messages)

        return response.content