import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify, render_template

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

@app.route("/")
def home():
    return render_template("index.html")

print("Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading vector database...")
index = faiss.read_index("vector.index")

with open("documents.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines()]

print("Loading language model...")
qa_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=120
)

def ask_bot(question, top_k=3, similarity_threshold=1.0):

    greetings = [
        "hi", "hello", "hey", "hii", "hola",
        "good morning", "good evening", "good afternoon"
    ]

    if question.lower().strip() in greetings:
        return "Hi 👋 I’m your C++ assistant. What’s on your mind today?"

    # Normal RAG flow
    q_embedding = embedder.encode([question])
    distances, indices = index.search(np.array(q_embedding), top_k)

    if distances[0][0] > similarity_threshold:
        return "I don't know based on the given data."

    context = "\n".join([documents[i] for i in indices[0]])

    prompt = f"""
Answer the question ONLY using the context below.
If the answer is not present, reply exactly:
I don't know based on the given data.

Context:
{context}

Question:
{question}

Answer:
"""

    output = qa_model(prompt)[0]["generated_text"].strip()
    return output


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"answer": "Please provide a question."})

    answer = ask_bot(question)
    return jsonify({"answer": answer})


# -------------------------------
@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    message = data.get("feedback", "")
    user_email = data.get("email", "Not provided")

    YOUR_EMAIL = os.getenv("EMAIL")
    YOUR_APP_PASSWORD = os.getenv("EMAIL_PASSWORD")

    msg = MIMEText(f"""
New Feedback Received from C++ Bot 🚀

User Email: {user_email}

Feedback:
{message}
""")

    msg["Subject"] = "New Feedback from C++ Bot"
    msg["From"] = YOUR_EMAIL
    msg["To"] = YOUR_EMAIL

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(YOUR_EMAIL, YOUR_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return jsonify({"status": "success"})
    except Exception as e:
        print("Email error:", e)
        return jsonify({"status": "error"})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

