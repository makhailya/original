import pytest

@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "CANCELED", "date": "2023-03-11T02:26:18.671407"},
        {"id": 3, "state": "EXECUTED", "date": "2022-03-11T02:26:18.671407"},
    ]