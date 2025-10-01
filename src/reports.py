# src/reports.py
import json
import logging
from datetime import datetime, timedelta
from typing import Optional
import pandas as pd

logger = logging.getLogger(__name__)


def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> str:
    """
    Возвращает траты по заданной категории за последние 3 месяца от переданной даты.

    Args:
        transactions (pd.DataFrame): Датафрейм с транзакциями.
        category (str): Название категории.
        date (str, optional): Дата в формате "YYYY-MM-DD". По умолчанию текущая дата.

    Returns:
        str: JSON-строка с суммой трат по категории.
    """
    # Определяем дату отсчета
    if date:
        end_date = datetime.strptime(date, "%Y-%m-%d")
    else:
        end_date = datetime.now()

    start_date = end_date - timedelta(days=90)

    logger.info(f"Анализ категории '{category}' за период {start_date.date()} - {end_date.date()}")

    # Фильтрация по дате и категории
    filtered = transactions[
        (pd.to_datetime(transactions["Дата операции"]) >= start_date) &
        (pd.to_datetime(transactions["Дата операции"]) <= end_date) &
        (transactions["Категория"] == category)
    ]

    total_spent = filtered["Сумма платежа"].sum()

    result = {"category": category, "total_spent": round(float(total_spent), 2)}

    logger.info(f"Траты по категории '{category}': {result['total_spent']}")

    return json.dumps(result, ensure_ascii=False, indent=2)
