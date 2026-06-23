import pandas as pd

df = pd.read_excel(
    "data/knowledge_mapping/knowledge_mapping.xlsx"
)

df.to_excel(
    "dataset/final/policy_dataset.xlsx",
    index=False
)

df.to_json(
    "dataset/final/policy_dataset.json",
    orient="records",
    indent=4
)

print(
    "Dataset Export Completed"
)