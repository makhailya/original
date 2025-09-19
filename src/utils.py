from pathlib import Path
import json
from typing import Any

def load_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    :param file_path: путь до файла
    :return: список словарей с транзакциями
    """
    path = Path(file_path)
    if not path.exists() or path.stat().st_size == 0:
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, OSError):
        return []

    return []
