# Imports

from metadata.metadata_search import metadata_search

from prompts.prompt_builder import build_prompt

from rag.retriever import retriever

from llm.llama_loader import (
    tokenizer,
    model
)

# Step 1
def retrieve_context(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context


# Step 2
def generate_response(
    context,
    question
):

    prompt = build_prompt(
        context,
        question
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.2,
        do_sample=False
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response


# Step 3
def ask_appx(question):

    meta_answer = metadata_search(
        question
    )

    if meta_answer:

        return meta_answer

    context = retrieve_context(
        question
    )

    answer = generate_response(
        context,
        question
    )

    return answer


# Step 4
if __name__ == "__main__":

    while True:

        question = input(
            "\nAsk Question: "
        )

        if question.lower() == "exit":

            break

        answer = ask_appx(
            question
        )

        print("\nAnswer:\n")

        print(answer)