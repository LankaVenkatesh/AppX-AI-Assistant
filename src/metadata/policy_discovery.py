import pandas as pd

METADATA_FILE = (
    "data/knowledge_mapping/"
    "policy_metadata.xlsx"
)

metadata_df = pd.read_excel(
    METADATA_FILE
)

def discover_policy(
    category
):

    category = category.lower()

    filtered_df = metadata_df[
        metadata_df[
            "category"
        ]
        .str.lower()
        ==
        category
    ]

    if filtered_df.empty:

        return (
            "No policies found."
        )

    return (
        filtered_df[
            "policy_name"
        ]
        .tolist()
    )