"""
Модуль для маскировки номеров карт и счетов.
"""


def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает маску для номера банковской карты.

    Первые 6 и последние 4 цифры остаются видимыми,
    а остальные заменяются на звездочки.
    Формат: XXXX XX** **** XXXX

    :param card_number: Полный номер карты в виде строки.
    :return: Маскированный номер карты.
    """
    if len(card_number) < 10 or not card_number.isdigit():
        raise ValueError("Некорректный номер карты")

    first_six = card_number[:6]
    last_four = card_number[-4:]
    return f"{first_six[:4]} {first_six[4:]}** **** {last_four}"


def get_mask_account(account_number: str) -> str:
    """
    Возвращает маску для номера банковского счета.

    Показывает только последние 4 цифры с двумя звездочками перед ними.
    Формат: **XXXX

    :param account_number: Полный номер счета в виде строки.
    :return: Маскированный номер счета.
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Некорректный номер счета")

    return f"**{account_number[-4:]}"
