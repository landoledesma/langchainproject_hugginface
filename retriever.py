from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from rich.console import Console
from langchain.chat_models import ChatOpenAI
console = Console()

def load_llm():
    llm  = ChatOpenAI(
        max_tokens=1000,
        temperature=0.2
        )
    return llm

def process_qa_query(query, retriever, llm):
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever
    )
    console.print("[yellow]La IA estÃ¡ pensando...[/yellow]")
    return qa_chain.run(query)

def process_memory_query(query, retriever, llm, chat_history):
    conversation = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, verbose=True
    )
    console.print("[yellow]La IA estÃ¡ pensando...[/yellow]")
    print(f"La historia antes de esta respuesta es: {chat_history}")
    result = conversation({"question": query, "chat_history": chat_history})
    chat_history.append((query, result["answer"]))
    return result["answer"]

