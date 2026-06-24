from pathlib import Path

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

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

text_splitter = (
    RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
)

chunks = []

for document in all_documents:

    split_chunks = (
        text_splitter.split_text(
            document["content"]
        )
    )

    for chunk in split_chunks:

        chunks.append(
            {
                "policy_name":
                document[
                    "policy_name"
                ],

                "content":
                chunk
            }
        )

print(
    "Total Chunks:",
    len(chunks)
)

print(
    chunks[0]["content"]
)