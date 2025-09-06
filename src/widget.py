import datetime
from src.masks import get_mask_card_number, get_mask_account
"""
Модуль для отображения информации о картах и счетах
с использованием маскировки номеров.
"""


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от входной строки.
    """
    try:
        parts = info.split()
        number = parts[-1]  # последний элемент всегда номер
        name = " ".join(parts[:-1])  # всё, кроме номера — это название

        if info.startswith("Счет"):
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)

        return f"{name} {masked_number}"
    except Exception:
        return info  # если что-то пошло не так, вернуть исходное значение


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат "ДД.MM.ГГГГ".
    """
    try:
        date_obj = datetime.datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except Exception:
        return date_str  # если не дата — вернуть как есть
