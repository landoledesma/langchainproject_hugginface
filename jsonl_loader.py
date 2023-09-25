class DocsJSONLLoader:
    """
    Cargador de documentos de documentaciones en formato JSONL.

    Args:
        file_path (str): Ruta al archivo JSONL a cargar.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        """
        Carga los documentos de la ruta del archivo especificada durante la inicialización.

        Returns:
            Una lista de objetos Document.
        """
        with jsonlines.open(self.file_path) as reader:
            documents = []
            for obj in reader:
                page_content = obj.get("text", "")
                metadata = {
                    "title": obj.get("title", ""),
                    "repo_owner": obj.get("repo_owner", ""),
                    "repo_name": obj.get("repo_name", ""),
                }
                documents.append(Document(page_content=page_content, metadata=metadata))
        return documents