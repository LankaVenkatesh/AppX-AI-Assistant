from pathlib import Path
import pandas as pd
import json

INPUT_FILE = (
    "data/knowledge_mapping/"
    "knowledge_mapping.xlsx"
)

OUTPUT_FOLDER = Path(
    "data/knowledge_mapping"
)

OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

df = pd.read_excel(INPUT_FILE)

metadata_records = []

for _, row in df.iterrows():

    policy_name = row["policy_name"]

    category = row["category"]

    metadata_records.append(
        {
            "policy_name": policy_name,
            "category": category,
            "source": f"{policy_name}.pdf"
        }
    )

metadata_df = pd.DataFrame(
    metadata_records
)

metadata_df.drop_duplicates(
    inplace=True
)

metadata_df.to_excel(
    OUTPUT_FOLDER /
    "policy_metadata.xlsx",
    index=False
)

metadata_df.to_json(
    OUTPUT_FOLDER /
    "policy_metadata.json",
    orient="records",
    indent=4
)

print(
    "Metadata Creation Completed"
)

print(
    f"Policies: {len(metadata_df)}"
)