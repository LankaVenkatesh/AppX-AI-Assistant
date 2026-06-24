from pathlib import Path
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

def get_chunks():

    INPUT_FOLDER = Path(
        "data/cleaned_text"
    )

    all_documents = []

    for txt_file in INPUT_FOLDER.glob("*.txt"):

        with open(
            txt_file,
            "r",
            encoding="utf-8"
        ) as f:

            text = f.read()

        all_documents.append(
            {
                "policy_name":
                txt_file.stem,

                "content":
                text
            }
        )

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
    )

    chunks = []

    for document in all_documents:

        split_chunks = splitter.split_text(
            document["content"]
        )

        for chunk in split_chunks:

            chunks.append(chunk)

    return chunks