import os
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

RAW_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/raw"))
CHUNKS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data/parsed"))
os.makedirs(CHUNKS_DIR, exist_ok=True)

# Chunker setup
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " "]
)

def clean_text(text):
    return text.replace('\xa0', ' ').replace('\x00', '').strip()

def chunk_file(ticker):
    file_path = os.path.join(RAW_DIR, f"{ticker}_10k.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    cleaned = clean_text(text)
    chunks = text_splitter.create_documents([cleaned])

    # Save chunks
    out_path = os.path.join(CHUNKS_DIR, f"{ticker}_chunks.json")
    import json
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump([doc.dict() for doc in chunks], f, indent=2)

    print(f"✅ Chunked {ticker} into {len(chunks)} segments and saved to {out_path}")

if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "TSLA", "AMZN", "JPM", "NVDA", "WMT", "META", "KO", "PFE"]
    for ticker in tickers:
        try:
            chunk_file(ticker)
        except Exception as e:
            print(f"❌ Failed to process {ticker}: {str(e)}")
