from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from jsonl_loader import DocsJSONLLoader
from rich.console import Console

console = Console()

def load_documents(file_path:str):
    loader = DocsJSONLLoader(file_path)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        length_function = len,
        chunk_overlap=160
    )

    return text_splitter.split_documents(data)

def get_chroma_db(embeddings,documents,path,recreate_chroma_db):
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