from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.writer_prompt import WRITER_SYSTEM_PROMPT



class WriterAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model = "gemini-2.0-flash",
            temperature = 0.7
        )
        
    
    def write(self , topic : str) -> str:
        
        messages = [
            ("system" , WRITER_SYSTEM_PROMPT),
            ("human" , topic)
            
        ]
        
        response = self.llm.invoke(messages)
        return response.content()