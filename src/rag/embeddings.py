from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

sample_text = """
Employees are entitled to
6 sick leaves annually.
"""

embedding = embedding_model.encode(
    sample_text
)

print(
    "Embedding Dimension:",
    len(embedding)
)

print(
    embedding[:10]
)