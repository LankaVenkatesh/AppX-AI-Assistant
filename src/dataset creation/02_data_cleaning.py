from pathlib import Path
import re

INPUT_FOLDER = Path("data/extracted_text")
OUTPUT_FOLDER = Path("data/cleaned_text")

OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

def clean_text(text):

    text = text.replace("\n", " ")

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()

for txt_file in INPUT_FOLDER.glob("*.txt"):

    with open(
        txt_file,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    cleaned_text = clean_text(content)

    output_file = (
        OUTPUT_FOLDER /
        txt_file.name
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(cleaned_text)

print("Data Cleaning Completed")