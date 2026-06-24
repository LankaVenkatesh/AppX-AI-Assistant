# ==========================================
# AppX AI Assistant - RAG Pipeline
# ==========================================

import sys
import os
import ollama

# Add src folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from metadata.metadata_search import metadata_search
from prompt_builder import build_prompt
from retriever import retriever


# ------------------------------------------
# Step 1 - Retrieve Context
# ------------------------------------------

def retrieve_context(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context


# ------------------------------------------
# Step 2 - Generate Response
# ------------------------------------------

def generate_response(
    context,
    question
):

    prompt = build_prompt(
        context,
        question
    )

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# ------------------------------------------
# Step 3 - Main AppX Logic
# ------------------------------------------

def ask_appx(question):

    meta_answer = metadata_search(question)

    if meta_answer:
        return meta_answer

    context = retrieve_context(question)

    answer = generate_response(
        context,
        question
    )

    return answer


# ------------------------------------------
# Step 4 - Run Application
# ------------------------------------------

if __name__ == "__main__":

    print("\n===== AppX AI Assistant =====")

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":

            print("\nExiting AppX Assistant...")
            break

        answer = ask_appx(question)

        print("\nAnswer:\n")
        print(answer)