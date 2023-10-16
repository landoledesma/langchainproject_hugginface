from langchain.vectorstores import Chroma
from rich.console import Console
from utils import get_query_from_user
from retriever import process_memory_query,process_qa_query,load_llm
from utils import get_file_path,chroma_docs
from langchain.embeddings import OpenAIEmbeddings
from ingest import get_chroma_db,load_documents
from dotenv import load_dotenv
import os
import time 

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

console = Console()

chat_type = "qa"

def run_conversation(vectorstore, chat_type, llm):

    console.print(
        "\n[blue]IA:[/blue] Hola ðŸš€! QuÃ© quieres preguntarme sobre Transformers e inteligencia artificial en general?"
    )

    if chat_type == "qa":
        console.print(
            "\n[green]EstÃ¡s utilizando el chatbot en modo de preguntas y respuestas. Este chatbot genera respuestas basÃ¡ndose puramente en la consulta actual sin considerar el historial de la conversaciÃ³n.[/green]"
        )
    elif chat_type == "memory_chat":
        console.print(
            "\n[green]EstÃ¡s utilizando el chatbot en modo de memoria. Este chatbot genera respuestas basÃ¡ndose en el historial de la conversaciÃ³n y en la consulta actual.[/green]"
        )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    chat_history = []

    while True:
        console.print("\n[blue]TÃº:[/blue]")
        query = get_query_from_user()

        if query.lower() == "salir":
            break

        if chat_type == "qa":
            response = process_qa_query(query=query, retriever=retriever, llm=llm)

        elif chat_type == "memory_chat":
            response = process_memory_query(
                query=query, retriever=retriever, llm=llm, chat_history=chat_history
            )

        console.print(f"[red]IA:[/red] {response}")

def main():
    chroma_exist = chroma_docs()
    
    documents = load_documents(get_file_path())

    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore_chroma = get_chroma_db(embeddings, documents, "chroma_docs",recreate_chroma_db=chroma_exist)
    console.print(f"[green]Documentos {len(documents)} cargados.[/green]")
    
    llm = load_llm()

    run_conversation(vectorstore_chroma, chat_type, llm)


if __name__ == "__main__":
    main()
