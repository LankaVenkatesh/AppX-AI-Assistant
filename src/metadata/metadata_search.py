import pandas as pd

METADATA_FILE = (
    "data/knowledge_mapping/"
    "policy_metadata.xlsx"
)

metadata_df = pd.read_excel(
    METADATA_FILE
)

def metadata_search(question):

    question = question.lower()

    if (
        "how many policies"
        in question
    ):

        return (
            f"There are "
            f"{len(metadata_df)} "
            f"policies available."
        )

    if (
        "list policies"
        in question
    ):

        policies = (
            metadata_df[
                "policy_name"
            ]
            .tolist()
        )

        return "\n".join(
            policies
        )

    if (
        "categories"
        in question
    ):

        categories = (
            metadata_df[
                "category"
            ]
            .unique()
            .tolist()
        )

        return "\n".join(
            categories
        )

    return None