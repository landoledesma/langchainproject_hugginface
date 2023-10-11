import json
import os
import re
import emoji
import requests
from termcolor import colored

def preprocess_text(text: str) -> str:
    """
    Preprocesa el texto eliminando ciertos patrones y caracteres.
    Args:
        text (str): Texto a preprocesar.
    Returns:
        El texto preprocesado.
    """
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"Copyright.*", "", text)
    text = text.replace("\n", " ")
    text = emoji.demojize(text)
    text = re.sub(r":[a-z_&+-]+:", "", text)
    return text


def download_file(url: str, repo_info: dict, jsonl_file_name: str) -> None:
    """
    Descarga un archivo desde una URL y lo guarda en un archivo JSONL.
    Args:
        url (str): URL desde donde se descarga el archivo.
        repo_info (dict): Información sobre el repositorio desde donde se descarga el archivo.
        jsonl_file_name (str): Nombre del archivo JSONL donde se guarda el archivo descargado.
    """
    response = requests.get(url)
    filename = url.split("/")[-1]
    text = response.text

    if text is not None and isinstance(text, str):
        text = preprocess_text(text)
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        file_dict = {
            "title": filename,
            "repo_owner": repo_info["owner"],
            "repo_name": repo_info["repo"],
            "text": text,
        }

        with open(jsonl_file_name, "a") as jsonl_file:
            jsonl_file.write(json.dumps(file_dict) + "\n")
    else:
        print(f"Texto no esperado: {text}")
