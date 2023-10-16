from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from jsonl_loader import DocsJSONLLoader
from rich.console import Console
from dotenv import load_dotenv
from utils import get_file_path
import os
import time 

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

console = Console()

recreate_chroma_db = False


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
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
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
def main():
    documents = load_documents(get_file_path())
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

    

    console.print(f"[green]Documentos {len(documents)} cargados.[/green]")
    
if __name__ == "__main__":
    main()
