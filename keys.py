import os
import sys

import jsonlines
import yaml
from langchain.schema import Document





def load_config():
    """
    Carga la configuración de la aplicación desde el archivo 'config.yaml'.

    Returns:
        Un diccionario con la configuración de la aplicación.
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_dir, "config.yaml")) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def get_openai_api_key():
    """
    Obtiene la clave API de OpenAI del entorno. Si no está disponible, detiene la ejecución del programa.

    Returns:
        La clave API de OpenAI.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("Por favor crea una variable de ambiente OPENAI_API_KEY.")
        sys.exit()
    return openai_api_key


def get_cohere_api_key():
    """
    Obtiene la clave API de Cohere del entorno. Si no está disponible, solicita al usuario que la ingrese.

    Returns:
        La clave API de Cohere.
    """
    cohere_api_key = os.getenv("COHERE_API_KEY")
    if not cohere_api_key:
        cohere_api_key = input("Por favor ingresa tu COHERE_API_KEY: ")
    return cohere_api_key


