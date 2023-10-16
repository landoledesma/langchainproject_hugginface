from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from rich.console import Console
from utils import get_query_from_user
from retriever import process_memory_query,process_qa_query
from ingest import get_chroma_db
console = Console()

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

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.2,
        max_tokens=1000,
    )

    vectorstore_chroma = get_chroma_db(embeddings, documents, "chroma_docs")
    run_conversation(vectorstore_chroma, chat_type, llm)


if __name__ == "__main__":
    main()
