from langchain_core.tools import tool
from langchain_core.runnables.config import RunnableConfig

from documents.models import Document

from typing import Dict, List


# List all active document
@tool
def list_documents(config: RunnableConfig) -> List:
    """Get a list of most recent 5 active documents from database

    Args:
       config(RunnableConfig): configuration needed as Runnable Config (Required)

    Returns:
        A list of dict that document id, title, content and updated_at timestamp
    """

    limit: int = 5
    configurable = config.get("configurable") or config.get("metadata")
    user_id = configurable.get("user_id") if configurable is not None else None

    if user_id is None:
        raise Exception("Invalid request for user.")

    query_set = Document.objects.filter(owner_id=user_id, active=True).order_by(
        "-created_at"
    )
    response_data = []

    for obj in query_set[:limit]:
        response_data.append(
            {
                "id": obj.id,  # type: ignore
                "title": obj.title,
                "content": obj.content,
                "updated_at": obj.updated_at,
            }
        )
    return response_data


@tool
def get_document(document_id: int, config: RunnableConfig) -> Dict:
    """Retrieve a single document from database by its respective id

    Args:
        document_id(int): The unique identifier of document (Required)
        config(RunnableConfig): The configuration needed as Runnable Config (Required)

    Returns:
        A dict that contains document id, title, content and updated_at timestamp
    """

    configurable = config.get("configurable") or config.get("metadata")
    user_id = configurable.get("user_id") if configurable is not None else None

    if user_id is None:
        raise Exception("Invalid request for user.")

    try:
        obj = Document.objects.get(id=document_id, owner_id=user_id, active=True)
    except Document.DoesNotExist:
        raise Exception("Document not found, try again")
    except Exception:
        raise Exception("Invalid request for document details, try again")

    response_data = {
        "id": obj.id,  # type: ignore
        "title": obj.title,
        "content": obj.content,
        "updated_at": obj.updated_at,
    }
    return response_data


@tool
def create_document(title: str, content: str, config: RunnableConfig) -> Dict:
    """Create and save a new document into database for specific user.

    Args:
        title(str): The document title string with max length of 120 characters (Required)
        content(str): The document content in long form of string with max length of 500 characters (Required)
        config(RunnableConfig): The configuration needed as Runnable Config (Required)

    Returns:
        A dict that contains newly created document id, title, content and created_at timestamp
    """

    configurable = config.get("configurable") or config.get("metadata")
    user_id = configurable.get("user_id") if configurable is not None else None

    if user_id is None:
        raise Exception("Invalid request for user.")

    try:
        obj = Document.objects.create(
            title=title, content=content, owner_id=user_id, active=True
        )
        obj.save()
    except Exception:
        raise Exception("Failed to add document into DB, try again")

    response_data = {
        "id": obj.id,  # type: ignore
        "title": obj.title,
        "content": obj.content,
        "created_at": obj.created_at,
    }
    return response_data
