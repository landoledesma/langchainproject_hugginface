import os
import yaml
from langchain.schema import Document

def load_config():
    """
    Carga la configuración de la aplicación desde el archivo 'config.yaml'.

    Returns:
        Un diccionario con la configuración de la aplicación.
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_dir,"config.yaml")) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLERROR as exc:
            print(exc)

def get_file_path():
    """
    Obtiene la ruta al archivo de base de datos JSONL especificado en la configuración de la aplicación.

    Returns:
        La ruta al archivo de base de datos JSONL.
    """
    config = load_config()
    root_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.join(root_dir)

    return os.path.join(parent_dir,config["jsonl_database_path"])

def create_dir(path:str) -> None:
    """
    Crea un directorio si no existe.

    Args:
        path (str): Ruta del directorio a crear.
    """
    if not os.path.exists(path):
        os.mkdir(path)

def remove_existing_file(file_path:str) -> None:
    """
    Elimina un archivo si existe.

    Args:
        file_path (str): Ruta del archivo a eliminar.
    """
    if os.path.exists(file_path):
        os.remove(file_path)

def get_query_from_user() -> str:
    """
    Solicita una consulta al usuario.

    Returns:
        La consulta ingresada por el usuario.
    """
    try:
        query = input()
        return query
    except EOFError:
        print("Error:Input no esperado. Intente de nuevo")
        return get_query_from_user()


def chroma_docs():
    # Obtiene la ruta del directorio donde se encuentra este script
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta completa al directorio "chroma_docs" dentro de esa carpeta
    path_chroma_docs = os.path.join(carpeta_actual, "chroma_docs")

    # Verifica si el directorio existe
    existe_chroma_docs = os.path.isdir(path_chroma_docs)

    return existe_chroma_docs
