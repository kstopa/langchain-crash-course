# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
#model = ChatOpenAI(model="gpt-4o")
model = ChatOllama(model="gemma3:12b")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
