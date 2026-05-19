import pytest
import sys
import os

# добавляем src в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "CANCELED", "date": "2023-03-11T02:26:18.671407"},
        {"id": 3, "state": "EXECUTED", "date": "2022-03-11T02:26:18.671407"},
    ]
