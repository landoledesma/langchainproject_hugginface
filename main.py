from rich.console import Console
from retriever import load_llm
from utils import get_file_path,chroma_docs
from langchain.embeddings import OpenAIEmbeddings
from ingest import get_chroma_db,load_documents
from dotenv import load_dotenv
import os
from conversation import get_chat_type,run_conversation

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

console = Console()

def main():
    chat_type = get_chat_type()
    chroma_exist = chroma_docs()
    
    documents = load_documents(get_file_path())

    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore_chroma = get_chroma_db(embeddings, documents, "chroma_docs",recreate_chroma_db=chroma_exist)
    console.print(f"[green]Documentos {len(documents)} cargados.[/green]")
    
    llm = load_llm()

    run_conversation(vectorstore_chroma, chat_type, llm)


if __name__ == "__main__":
    main()