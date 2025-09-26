from datetime import datetime
from typing import Any


def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO-строки в формат 'ДД.ММ.ГГГГ'.
    Если парсинг неудачен — возвращает исходную строку.
    """
    if not date_str or not isinstance(date_str, str):
        return ""
    try:
        # Если есть 'T' — берём только часть до T (дата)
        if "T" in date_str:
            date_part = date_str.split("T", 1)[0]
            d = datetime.fromisoformat(date_part)
            return d.strftime("%d.%m.%Y")
        # попытка распарсить как YYYY-MM-DD
        d = datetime.fromisoformat(date_str)
        return d.strftime("%d.%m.%Y")
    except Exception:
        try:
            # последний шанс: взять первые 10 символов и распарсить
            date_part = date_str[:10]
            d = datetime.strptime(date_part, "%Y-%m-%d")
            return d.strftime("%d.%m.%Y")
        except Exception:
            # если всё плохо — вернём строку как есть
            return date_str
