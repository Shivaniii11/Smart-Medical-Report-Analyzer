from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings

class LocalEmbeddings(Embeddings):
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, text):
        return self.model.encode([text])[0].tolist()

def build_db(text):

    if not text.strip():
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    if not chunks:
        return None

    return FAISS.from_texts(chunks, LocalEmbeddings())