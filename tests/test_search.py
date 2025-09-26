from src.search import process_bank_search, process_bank_operations


def test_process_bank_search():
    data = [{"description": "Открытие вклада"}, {"description": "Перевод"}, {"description": "Снятие"}]
    result = process_bank_search(data, "вклад")
    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"


def test_process_bank_operations():
    data = [
        {"description": "Открытие вклада"},
        {"description": "Перевод"},
        {"description": "Перевод"},
    ]
    result = process_bank_operations(data, ["Открытие", "Перевод"])
    assert result == {"Открытие": 1, "Перевод": 2}
