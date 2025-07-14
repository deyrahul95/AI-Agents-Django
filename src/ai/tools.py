from langchain_core.tools import tool

from documents.models import Document


# List all active document
@tool
def list_documents():
    """Get a list of active documents"""
    query_set = Document.objects.filter(active=True)
    response_data = []
    for obj in query_set:
        response_data.append(
            {
                "id": obj.id,  # type: ignore
                "title": obj.title,
                "content": obj.content,
            }
        )
    return response_data


@tool
def get_document(document_id: int):
    """Get a single document by its respective id

    Params:
        document_id: The unique identifier of document
    """
    obj = Document.objects.get(id=document_id, active=True)
    response_data = {
        "id": obj.id,  # type: ignore
        "title": obj.title,
        "content": obj.content,
    }
    return response_data
