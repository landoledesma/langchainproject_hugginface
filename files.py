def get_file_path():
    """
    Obtiene la ruta al archivo de base de datos JSONL especificado en la configuración de la aplicación.

    Returns:
        La ruta al archivo de base de datos JSONL.
    """
    config = load_config()

    root_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.join(root_dir, "..")

    return os.path.join(parent_dir, config["jsonl_database_path"])


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
        print("Error: Input no esperado. Por favor intenta de nuevo.")
        return get_query_from_user()


def create_dir(path: str) -> None:
    """
    Crea un directorio si no existe.

    Args:
        path (str): Ruta del directorio a crear.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def remove_existing_file(file_path: str) -> None:
    """
    Elimina un archivo si existe.

    Args:
        file_path (str): Ruta del archivo a eliminar.
    """
    if os.path.exists(file_path):
        os.remove(file_path)