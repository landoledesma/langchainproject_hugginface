from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from jsonl_loader import DocsJSONLLoader
from rich.console import Console
from dotenv import load_dotenv
from utils import get_file_path,get_query_from_user
import os
import time 

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstore/db_faiss"

console = Console()

recreate_chroma_db = False
chat_type = "memory_chat"

def load_documents(file_path:str):
    loader = DocsJSONLLoader(file_path)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        length_function = len,
        chunk_overlap=160
    )

    return text_splitter.split_documents(data)

def get_chroma_db(embeddings,documents,path):

    if recreate_chroma_db:
        console.print("Recreando CHROMA DB")
        return Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=path
        )
    else:
        console.print("Cargando base chroma")
        return Chroma(persist_directory=path,
                      embedding_function=embeddings)
    