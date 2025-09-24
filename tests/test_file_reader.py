import pandas as pd

from src.file_reader import read_transactions_csv, read_transactions_excel


def test_read_transactions_csv(tmp_path, monkeypatch):
    # создаём временный CSV
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("id,amount,currency\n1,100,USD\n2,200,RUB\n")

    result = read_transactions_csv(csv_file)
    assert isinstance(result, list)
    assert result[0]["id"] == 1
    assert result[0]["currency"] == "USD"


def test_read_transactions_excel(tmp_path):
    # создаём временный Excel
    excel_file = tmp_path / "test.xlsx"
    df = pd.DataFrame([{"id": 1, "amount": 100, "currency": "USD"}])
    df.to_excel(excel_file, index=False)

    result = read_transactions_excel(excel_file)
    assert isinstance(result, list)
    assert result[0]["amount"] == 100


def test_csv_file_not_found():
    assert read_transactions_csv("no_file.csv") == []


def test_excel_file_not_found():
    assert read_transactions_excel("no_file.xlsx") == []
