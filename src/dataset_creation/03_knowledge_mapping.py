from pathlib import Path
import pandas as pd

INPUT_FOLDER = Path("data/cleaned_text")

records = []

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(
        txt_file,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    records.append({

        "policy_name":
        txt_file.stem,

        "category":
        "HR",

        "content":
        content
    })

df = pd.DataFrame(records)

df.to_excel(
    "data/knowledge_mapping/knowledge_mapping.xlsx",
    index=False
)

print(
    "Knowledge Mapping Completed"
)