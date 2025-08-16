"""
Модуль для отображения информации о картах и счетах
с использованием маскировки номеров.
"""

from masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от входной строки.

    Если строка начинается со слова "Счет", применяется маска для счета.
    В остальных случаях предполагается, что это карта, и применяется
    маска для карты.

    :param info: Строка с типом и номером карты/счета
                 (например, "Visa Platinum 7000792289606361"
                 или "Счет 73654108430135874305").
    :return: Строка с замаскированным номером.
    """
    parts = info.split()
    number = parts[-1]  # последний элемент всегда номер
    name = " ".join(parts[:-1])  # всё, кроме номера — это название

    if info.startswith("Счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


from datetime import datetime


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO "YYYY-MM-DDTHH:MM:SS.ssssss"
    в формат "ДД.MM.ГГГГ".

    :param date_str: Строка с датой, например "2024-03-11T02:26:18.671407".
    :return: Строка с датой в формате "ДД.MM.ГГГГ", например "11.03.2024".
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
