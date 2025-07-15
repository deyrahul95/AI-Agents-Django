from langgraph.prebuilt import create_react_agent

from ai.llms import get_openai_model
from ai.tools import create_document, get_document, list_documents


def get_document_agent(checkpointer=None):
    model = get_openai_model()
    document_tools = [list_documents, get_document, create_document]

    agent = create_react_agent(
        model=model,
        tools=document_tools,
        prompt="You are a helpful assistant in managing a user's documents within this app",
        checkpointer=checkpointer,
    )
    return agent
