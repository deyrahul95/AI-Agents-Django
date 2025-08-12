from django.conf import settings
from langchain_openai import ChatOpenAI


def get_openai_model(model: str = "qwen3:1.7b") -> ChatOpenAI:
    """Get an open ai model

    Args:
        model: model you want to load default is 'qwen3:1.7b'

    Returns:
        An instance of ChatOpenAI
    """

    openai_model = ChatOpenAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=settings.OPENAI_API_KEY,
        base_url=settings.OPENAI_BASE_URL,
    )
    return openai_model