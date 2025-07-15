from django.conf import settings
from langchain_openai import ChatOpenAI


def get_openai_model(model="llama3.2") -> ChatOpenAI:
    """Get an open ai model

    Params:
        model: model you want to load default is 'llama:3.2'
    """

    return ChatOpenAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=settings.OPENAI_API_KEY,
        base_url=settings.OPENAI_BASE_URL,
    )
