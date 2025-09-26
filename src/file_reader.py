# src/file_reader.py
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
from typing import Any

def read_transactions_csv(path: str) -> list[dict[str, Any]]:
    df = pd.read_csv(path)
    return df.to_dict(orient="records")  # type: ignore

def read_transactions_excel(path: str) -> list[dict[str, Any]]:
    df = pd.read_excel(path)
    return df.to_dict(orient="records")  # type: ignore
