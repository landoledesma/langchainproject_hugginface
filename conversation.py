from rich.console import Console
from retriever import process_memory_query,process_qa_query
from utils import get_query_from_user

console = Console()


def get_chat_type():
    while True:
        user_input = input("Enter chat type (qa or memory_chat): ").strip().lower()
        if user_input in ["qa", "memory_chat"]:
            return user_input
        else:
            print("Invalid option. Please enter either 'qa' or 'memory_chat'.")


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

