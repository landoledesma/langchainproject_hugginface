import requests
from termcolor import colored
from text_extractor import download_file
from typing import Dict
import os

def process_directory(
    path: str,
    repo_info: Dict,
    headers: Dict,
    jsonl_file_name: str,
) -> None:
    """
    Procesa un directorio de un repositorio de GitHub y descarga los archivos en él.
    Args:
        path (str): Ruta del directorio a procesar.
        repo_info (Dict): Información sobre el repositorio que contiene el directorio.
        headers (Dict): Headers para la petición a la API de GitHub.
        jsonl_file_name (str): Nombre del archivo JSONL donde se guardarán los archivos descargados.
    """
    # Si el nombre del directorio es 'zh', lo omite y retorna inmediatamente.
    # Esta característica está implementada para no descargar las traducciones en chino.
    if os.path.basename(path) == "zh":
        print(
            colored(
                f"Se omite el directorio 'zh' (traducciones en chino): {path}", "yellow"
            )
        )
        return

    base_url = f"https://api.github.com/repos/{repo_info['owner']}/{repo_info['repo']}/contents/"
    print(
        colored(f"Procesando directorio: {path} del repo: {repo_info['repo']}", "blue")
    )
    response = requests.get(base_url + path, headers=headers)

    if response.status_code == 200:
        files = response.json()
        for file in files:
            if file["type"] == "file" and (
                file["name"].endswith(".mdx") or file["name"].endswith(".md")
            ):
                print(colored(f"Descargando documento: {file['name']}", "green"))
                print(colored(f"Descarga URL: {file['download_url']}", "cyan"))
                download_file(
                    file["download_url"],
                    repo_info,
                    jsonl_file_name,
                )
            elif file["type"] == "dir":
                process_directory(
                    file["path"],
                    repo_info,
                    headers,
                    jsonl_file_name,
                )
        print(colored("Exito en extracción de documentos del directorio.", "green"))
    else:
        print(
            colored(
                "No se pudieron recuperar los archivos. Verifique su token de GitHub y los detalles del repositorio.",
                "red",
            )
        )