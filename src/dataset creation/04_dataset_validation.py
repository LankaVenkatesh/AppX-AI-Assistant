import pandas as pd

df = pd.read_excel(
    "data/knowledge_mapping/knowledge_mapping.xlsx"
)

print("\nTotal Records:")
print(len(df))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nColumns:")
print(df.columns.tolist())

print(
    "\nDataset Validation Completed"
)