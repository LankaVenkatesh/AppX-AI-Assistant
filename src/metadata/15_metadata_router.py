from metadata_search import (
    metadata_search
)

def check_metadata_question(
    question
):

    result = metadata_search(
        question
    )

    if result:

        return result

    return None