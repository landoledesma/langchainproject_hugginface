import os
import datetime
import sys
sys.path.append("..")  # añadir el directorio padre al PATH
from utils import create_dir, load_config, remove_existing_file
from process_directory import process_directory

def main():
    """
    Función principal que se ejecuta cuando se inicia el script.
    """
    config = load_config()
    github_token = os.getenv("GITHUB_TOKEN")

    if github_token is None:
        raise ValueError(
            "GITHUB_TOKEN no está configurado en las variables de entorno."
        )

    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3.raw",
    }

    current_date = datetime.date.today().strftime("%Y_%m_%d")
    jsonl_file_name = f"data/docs_en_{current_date}.jsonl"

    create_dir("data/")
    remove_existing_file(jsonl_file_name)

    for repo_info in config["github"]["repos"]:
        process_directory(
            repo_info["path"],
            repo_info,
            headers,
            jsonl_file_name,
        )

if __name__ == "__main__":
    main()