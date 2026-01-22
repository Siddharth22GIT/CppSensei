# 🤖 CppSensei — Domain‑Trained AI Tutor

A **domain‑specific AI assistant** that answers C++ questions using a custom knowledge base with **Retrieval‑Augmented Generation (RAG)**.
Built with **Flask + FAISS + Sentence Transformers + HuggingFace**, wrapped in a modern glass‑style web UI with feedback, greetings, and monetization support.

---

## 🚀 Features

* 🧠 **Domain‑Trained AI** — answers only from a curated C++ knowledge base
* 🔎 **RAG Pipeline** — FAISS vector search + semantic embeddings
* 💬 **Modern Chat UI** — glassmorphism, bubbles, typing indicator
* 🤖 **Smart Greetings** — friendly responses to hi / hello / hey
* 🗑️ **Clear Chat Button** — instantly reset conversation
* 📖 **About Modal** — explains the system & tech stack
* 💬 **Feedback System** — users send feedback → delivered directly to your email
* ☕ **Buy Me a Coffee Button** — built‑in monetization
* 🔒 **Secure Secrets** — credentials stored in `.env` (never committed)
* 🎯 **Production‑style Structure** — clean backend + frontend separation

---

## 🧠 Architecture (How it Works)

```
User Browser
     │
     ▼
 Flask Web App  ──▶  /ask API
     │
     ▼
Sentence Transformer (Embeddings)
     │
     ▼
 FAISS Vector Database
     │
     ▼
Relevant C++ Context
     │
     ▼
FLAN‑T5 Language Model
     │
     ▼
 Answer Returned to UI
```

This is a full **Retrieval‑Augmented Generation (RAG)** pipeline.

---

## 🛠️ Tech Stack

### Backend

* Python 3.10+
* Flask
* FAISS (vector database)
* Sentence‑Transformers (`all-MiniLM-L6-v2`)
* HuggingFace Transformers (`google/flan-t5-base`)
* SMTP (Gmail feedback system)

### Frontend

* HTML + CSS (Glassmorphism UI)
* Vanilla JavaScript
* Modal system (About / Feedback)
* SVG Favicon support

---

## 📂 Project Structure

```
AI Agent/
├── app.py              # Main Flask server
├── embeddings.py       # Builds vector database from data.txt
├── chatbot.py          # CLI version (optional)
├── data/
│   └── data.txt        # C++ knowledge base
├── templates/
│   └── index.html      # Chat UI
├── static/
│   └── favicon.svg     # App favicon
├── .env                # Email credentials (NOT committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/cpp-bot.git
cd cpp-bot
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File (Email Feedback Setup)

In the project root, create a file named `.env`:

```env
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_16_digit_gmail_app_password
```

⚠️ This must be a **Gmail App Password**, not your normal Gmail password.

---

### 5️⃣ Prepare the Knowledge Base

Edit your C++ dataset:

```
data/data.txt
```

Then generate embeddings:

```bash
python embeddings.py
```

This creates:

* `vector.index`
* `documents.txt`

---

### 6️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Usage

* Ask any C++ question from the trained dataset
* Try greetings:

  ```
  hi
  hello
  ```
* Click 🗑️ to clear chat
* Use **Feedback** to send suggestions (arrives directly in your inbox)
* Click ☕ to support the project

---

## 🔒 Security

* `.env` is excluded via `.gitignore`
* Virtual environment (`venv/`) is not committed
* No API keys or passwords are exposed in the repository

---

## 🌐 Deployment (Optional)

This app can be deployed on:

* Render
* Railway
* HuggingFace Spaces
* Heroku (with worker config)

Just make sure to add environment variables on the hosting platform.

---

## 🛣️ Roadmap (Future Improvements)

* 📚 Multi‑subject support (Python, OS, DSA)
* 🧠 Chat history memory
* 📄 PDF upload → auto‑train knowledge base
* 🔐 User authentication
* ⚛️ React + Tailwind frontend
* 📊 Admin dashboard for feedback analytics

---

## 👨‍💻 Author

**Siddharth Mishra**

---

## ⭐ Acknowledgements

* HuggingFace Transformers
* Sentence‑Transformers
* FAISS by Facebook AI Research
* Flask Community

---

## 📜 License

This project is licensed under the MIT License — feel free to use, modify, and distribute.

---

🔥 If you like this project, don’t forget to **star ⭐ the repository** and share it!
