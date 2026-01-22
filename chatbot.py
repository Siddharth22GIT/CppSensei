from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

# -------------------------------
# Load embedding model
# -------------------------------
print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------------------
# Load vector database
# -------------------------------
print("Loading vector database...")
index = faiss.read_index("vector.index")

# -------------------------------
# Load stored documents
# -------------------------------
with open("documents.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines()]

# -------------------------------
# Load language model (correct pipeline)
# -------------------------------
print("Loading language model...")
qa_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=120
)

# -------------------------------
# Core QA function (SAFE VERSION)
# -------------------------------
def ask_bot(question, top_k=3, similarity_threshold=1.0):
    # Embed the question
    q_embedding = embedder.encode([question])

    # Search similar docs
    distances, indices = index.search(np.array(q_embedding), top_k)

    # If the closest result is too far → no relevant answer
    if distances[0][0] > similarity_threshold:
        return "I don't know based on the given data."

    # Retrieve context
    context = "\n".join([documents[i] for i in indices[0]])

    # Build strict prompt
    prompt = f"""
You are a domain question answering assistant.
Use ONLY the context below.
If the answer is not clearly present in the context, reply exactly:
I don't know based on the given data.

Context:
{context}

Question:
{question}

Answer:
"""

    # Generate answer
    output = qa_model(prompt)[0]["generated_text"].strip()

    # Extra safety: if model still copies context, block it
    if output.lower().startswith("flask") or output.lower().startswith("react") or output.lower().startswith("seo"):
        # crude but effective safety fallback
        if question.lower() not in context.lower():
            return "I don't know based on the given data."

    return output


# -------------------------------
# Chat loop
# -------------------------------
print("\nAI Agent ready. Type 'exit' to quit.\n")

while True:
    question = input("Ask: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    answer = ask_bot(question)
    print("\nBot:", answer, "\n")
