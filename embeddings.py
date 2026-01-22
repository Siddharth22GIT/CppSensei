from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Load embedding model
print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load training data
data_path = "data/data.txt"

with open(data_path, "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

print(f"Loaded {len(documents)} documents")

# Create embeddings
print("Creating embeddings...")
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save index and documents
faiss.write_index(index, "vector.index")

with open("documents.txt", "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc + "\n")

print("Vector database created successfully!")
