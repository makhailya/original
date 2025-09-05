import pytest
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state_default(sample_operations):
    result = filter_by_state(sample_operations)
    assert all(op["state"] == "EXECUTED" for op in result)
    assert len(result) == 2


def test_filter_by_state_canceled(sample_operations):
    result = filter_by_state(sample_operations, state="CANCELED")
    assert all(op["state"] == "CANCELED" for op in result)
    assert len(result) == 1


def test_filter_by_state_empty(sample_operations):
    result = filter_by_state(sample_operations, state="PENDING")
    assert result == []


def test_sort_by_date_desc(sample_operations):
    sort_by_date(sample_operations, reverse=True)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_asc(sample_operations):
    result = sort_by_date(sample_operations, reverse=False)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates)
