Thank you. Based on your full directory structure and actual implementation, here is a **professional, clean, and complete `README.md`** focused **only on your full-stack web application** – no mentions of Traderverse, LangGraph, or other unrelated tasks.

---

```markdown
# genai-sec10k-insights

**genai-sec10k-insights** is a full-stack Retrieval-Augmented Generation (RAG) web application that enables users to interactively query and analyze SEC 10-K filings from major companies. The system extracts key insights from long-form financial reports using a semantic search pipeline powered by OpenAI embeddings and a FAISS vector store, all deployed behind a FastAPI backend and custom frontend.

---

## 📌 Features

- 🔍 **Query Interface**: Users can ask questions in natural language and get context-aware answers from 10-K filings.
- 📄 **Document Source**: Uses real SEC 10-K filings from companies like AAPL, TSLA, JPM, etc.
- ⚙️ **Backend**: FastAPI-based API server with secure authentication and RAG pipeline.
- 🧠 **Vector Search**: OpenAI embeddings + FAISS index for fast and accurate semantic retrieval.
- 💻 **Frontend**: Custom HTML, CSS, and JavaScript interface with clean UI and dynamic response rendering.
- 🔐 **Authentication**: Random 6-digit terminal-generated access code required before accessing the app.

---

## 🗂️ Project Structure

```

genai-sec10k-insights/
├── backend/
│   └── app/
│       ├── main.py               # FastAPI entry point
│       ├── api\_routes.py         # API route handlers
│       ├── config.example.py     # Config template
│       └── rag\_pipeline.py       # RAG logic: load FAISS, embed, search
│
├── data/
│   ├── raw/                      # Raw 10-K filings (e.g., AAPL\_10k.txt)
│   ├── parsed/                   # Chunked JSON from raw filings
│   └── faiss\_index/             # Prebuilt FAISS index and mapping
│
├── sec\_downloader/              # Utility scripts
│   ├── download\_sec\_filings.py  # Scrapes and saves raw 10-Ks
│   ├── chunk\_text.py            # Splits long 10-K text into chunks
│   └── embed\_and\_store.py       # Embeds chunks and builds FAISS index
│
├── frontend/
│   ├── index.html               # Main chat UI
│   ├── auth.html                # Auth page with blur effect
│   ├── styles.css               # Styling for layout and animation
│   ├── app.js                   # Query + response logic (AJAX)
│   └── assets/                  # Fonts, icons, etc.
│
├── notebooks/
│   └── mock\_10k\_40\_questions.json  # Mock questions for testing
│
├── Dockerfile                   # Production-ready Docker image
├── requirements.txt             # Python dependencies
├── LICENSE
└── README.md                    # You're here!

````

---

## ⚙️ How It Works

### 1. Data Acquisition (`sec_downloader`)
- 10-K reports are downloaded using `download_sec_filings.py`.
- Files are stored in `data/raw/`.

### 2. Preprocessing
- `chunk_text.py` splits raw text into overlapping chunks with metadata.
- Output chunks saved as JSON in `data/parsed/`.

### 3. Embedding & Indexing
- `embed_and_store.py` uses OpenAI’s `text-embedding-3-small` model to embed parsed chunks.
- Embeddings stored in a FAISS index (`index.faiss` and `index.pkl`) under `data/faiss_index/`.

### 4. Backend (`backend/app`)
- `main.py` initializes FastAPI with secure cookie auth.
- `rag_pipeline.py` handles query embedding, similarity search via FAISS, and prompt construction.
- `api_routes.py` serves `/chat` route with POST support for queries.
- A random 6-digit access code is printed at app launch and must be entered to unlock the app.

### 5. Frontend (`frontend`)
- `auth.html`: Initial page prompts for access code with a blurred background.
- `index.html`: Interactive UI with user input box, loading animation, and styled answer display.
- `app.js`: Handles sending queries, receiving responses, and displaying them in real time.
- `styles.css`: Custom CSS for layout, transitions, and visual polish.

---

## 🚀 Running the App Locally

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/genai-sec10k-insights.git
cd genai-sec10k-insights
````

### 2. Set Up Environment

```bash
cd backend
cp app/config.example.py app/config.py
# Add your OpenAI API key and config in config.py
pip install -r requirements.txt
```

### 3. Run the App

```bash
cd backend
uvicorn app.main:app --reload
```

Access the app at: [http://localhost:8000/chat](http://localhost:8000/chat)

> ⚠️ Enter the access code displayed in the terminal on the `auth.html` page to unlock access.

### 4. (Optional) Docker Build

```bash
docker build -t genai-sec10k-app .
docker run -p 8000:8000 genai-sec10k-app
```

---

## 🔒 Authentication Mechanism

* When the FastAPI server starts, a secure 6-digit numeric access code is printed in the terminal.
* This must be entered on the frontend’s auth page before gaining access.
* Auth state is stored in cookies to protect `/chat` and `/docs`.

---

## 📊 Companies Covered

The app includes processed 10-K filings from the following companies:

* Apple (AAPL)
* Amazon (AMZN)
* JPMorgan Chase (JPM)
* Coca-Cola (KO)
* Meta (META)
* Microsoft (MSFT)
* NVIDIA (NVDA)
* Pfizer (PFE)
* Tesla (TSLA)
* Walmart (WMT)

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

```

---

Let me know if you'd like:
- A **shortened README** version for a landing page
- A **demo GIF or image placeholder**
- The access code system explained as a **separate doc (`AUTH.md`)**

Ready to drop into your GitHub as-is.
```
