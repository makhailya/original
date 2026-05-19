from __future__ import annotations

from typing import Any, Dict, List

import pandas as pd


def read_transactions_csv(path: str) -> List[Dict[str, Any]]:
    df = pd.read_csv(path)
    return df.to_dict(orient="records")  # type: ignore


def read_transactions_excel(path: str) -> List[Dict[str, Any]]:
    df = pd.read_excel(path)
    return df.to_dict(orient="records")  # type: ignore
