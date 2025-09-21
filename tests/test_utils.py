from utils import load_transactions


def test_load_transactions_valid_file(tmp_path):
    file = tmp_path / "data.json"
    file.write_text('[{"id": 1, "amount": 100}]', encoding="utf-8")
    assert load_transactions(str(file)) == [{"id": 1, "amount": 100}]


def test_load_transactions_empty_file(tmp_path):
    file = tmp_path / "data.json"
    file.write_text("", encoding="utf-8")
    assert load_transactions(str(file)) == []
