from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.editor_prompt import EDITOR_SYSTEM_PROMPT


class EditorAgent:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0.3
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