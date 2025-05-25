# genai-sec10k-insights

**genai-sec10k-insights** is a full-stack Retrieval-Augmented Generation (RAG) web application that enables users to interactively query and analyze SEC 10-K filings from major companies. The system extracts key insights from long-form financial reports using a semantic search pipeline powered by OpenAI embeddings and a FAISS vector store, all deployed behind a FastAPI backend and custom frontend.
#
![Screencastfrom2025-05-2510-10-20-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/b6b4568e-f80f-4dd6-9556-dce2333bffc7)

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
## 🚦 Step-by-Step Walkthrough

Follow this guided walkthrough to experience the full pipeline from server startup to querying a 10-K report:

---

### 🔁 1. Start the FastAPI Server

From the project root, run the backend using:

```bash
cd backend
uvicorn app.main:app --reload
````

Once started, you'll see a **well-formatted terminal output** styled using `rich`, including:

* Project banner
* Usage instructions
* Export variable tips
* A **random 6-digit authentication code**

Example:

```
🚀 genai-sec10k-insights is running on http://localhost:8000
🔒 Auth Code: 348215
🔗 Visit /chat to access the chatbot interface
```

---

### 🌐 2. Visit the Web App in Your Browser

Open:

```
http://localhost:8000
```

You’ll be taken to the **authentication screen** (`auth.html`) which has:

* A minimal design with blurred background
* An input field for the 6-digit code

Enter the code shown in your terminal and proceed.

---

### 💬 3. Access the Chatbot Interface

Once authenticated, you'll land on the **main chat interface** (`index.html`) where you can:

* Ask any question related to the SEC 10-K reports of the 10 companies
* View dynamic responses with smooth UI animations

---


### 📥 4. Use an Example Prompt (or Ask Your Own)

To help you get started, we’ve provided a few **sample prompts** in:

```

notebooks/mock\_10k\_40\_questions.json

````

Here’s one you can try immediately:

```json
{
  "question": "What does Microsoft report about cybersecurity risks?"
}
````

📌 **Important Note:**
These are just **example prompts** — the chatbot is **not limited** to answering only those.

Since this app is built on top of the **actual SEC 10-K filings** from 10 companies (AAPL, MSFT, TSLA, AMZN, etc.), you can ask **any meaningful financial or business-related question** that could be answered from those filings.

✅ For example:

* "What does Apple say about supply chain risks?"
* "How does Amazon describe its revenue streams?"
* "What litigation risks does Meta report?"

Just make sure your question is **relevant to the content typically found in 10-K reports** (i.e., risk factors, business overview, financials, strategy, etc.).

Once submitted, your question will be semantically searched across the embedded document chunks, and an accurate answer will be generated based on the most relevant 10-K sources.

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
git clone https://github.com/r0han01/genai-sec10k-insights.git
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

## 🛠️ Troubleshooting & Swagger Testing

If the frontend chatbot interface (`/chat`) does not seem to be working correctly (e.g., blank responses, stuck loading, or CORS errors), you can **directly test the backend API** using the built-in Swagger UI at:

```

http://localhost:8000/docs

````

### ✅ Why Use This?

- Confirms whether the backend and RAG pipeline are functioning correctly.
- Helps isolate whether issues originate from the **frontend** or **backend**.
- Allows developers to quickly debug request/response flow without modifying UI.

---

### 🧪 How to Test via Swagger

1. Make sure your FastAPI backend is running:
   ```bash
   uvicorn app.main:app --reload

2. Open your browser and go to:

   ```
   http://localhost:8000/docs
   ```

3. Scroll down to the `POST /ask` endpoint.

4. Click on **`Try it out`**.

5. In the request body, paste the following prompt:

   ```json
   {
     "question": "What does Microsoft report about cybersecurity risks?"
   }
   ```

6. Click **Execute**.

7. You should receive a structured JSON response:

   ```json
   {
     "answer": "Microsoft discusses cybersecurity risks related to...",
     "sources": [
       "MSFT_10k.txt"
     ]
   }
   ```

---

### 🧩 If It Works Here but Not in Frontend

If the Swagger `/ask` test returns valid responses but the frontend (`/chat`) does not:

* ✅ It means your **backend RAG pipeline is working fine**.
* ❌ The issue is likely in:

  * `frontend/app.js` (JavaScript fetch logic)
  * CORS configuration (make sure backend allows frontend origin)
  * Cookie or auth state mismatch

---

### 🔧 Recommended Fixes

* Check the console in browser dev tools (`F12`) for network or JS errors.
* Verify you're logged in with the correct 6-digit code.
* Ensure `fetch` requests from the frontend hit the same `/ask` endpoint with correct `Content-Type` headers.

---

By using the Swagger UI, you can verify your backend independently and streamline debugging efforts.

