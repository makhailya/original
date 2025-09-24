# src/file_reader.py
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pandas as pd


def read_transactions_csv(path: str) -> List[Dict[str, Any]]:
    """
    Считывает транзакции из CSV-файла и возвращает список словарей.
    Если файл не найден или пуст/невалиден — возвращает пустой список.
    """
    file = Path(path)
    if not file.exists():
        return []

    try:
        df = pd.read_csv(file)
        # Если дата в колонках — можно дополнительно обработать типы
        return df.to_dict(orient="records")
    except (pd.errors.EmptyDataError, pd.errors.ParserError, OSError):
        return []


def read_transactions_excel(path: str) -> List[Dict[str, Any]]:
    """
    Считывает транзакции из Excel (.xlsx) и возвращает список словарей.
    Если файл не найден или невалиден — возвращает пустой список.
    """
    file = Path(path)
    if not file.exists():
        return []

    try:
        df = pd.read_excel(file, engine="openpyxl")
        return df.to_dict(orient="records")
    except (ValueError, OSError):
        return []
