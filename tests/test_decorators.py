import pytest
from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    @log()
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "div error" in captured.out
    assert "Inputs: (1, 0)," in captured.out


def test_log_success_file(tmp_path):
    logfile = tmp_path / "test.log"

    @log(filename=str(logfile))
    def mul(a, b):
        return a * b

    result = mul(3, 4)
    assert result == 12

    with open(logfile, "r", encoding="utf-8") as f:
        content = f.read()

    assert "mul ok" in content


def test_log_error_file(tmp_path):
    logfile = tmp_path / "test.log"

    @log(filename=str(logfile))
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    with open(logfile, "r", encoding="utf-8") as f:
        content = f.read()

    assert "div error" in content
    assert "Inputs: (1, 0)," in content
