from pathlib import Path
from pypdf import PdfReader

PDF_FOLDER = Path("data/policies")
OUTPUT_FOLDER = Path("data/extracted_text")

OUTPUT_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

for pdf_file in PDF_FOLDER.glob("*.pdf"):

    print(f"Processing: {pdf_file.name}")

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    output_file = (
        OUTPUT_FOLDER /
        f"{pdf_file.stem}.txt"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(text)

print("Text Extraction Completed")