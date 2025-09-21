import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.
    Первые 6 и последние 4 цифры остаются видимыми.
    """
    if len(card_number) < 10 or not card_number.isdigit():
        logger.error("Некорректный номер карты: %s", card_number)
        raise ValueError("Некорректный номер карты")

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.debug("Маскирование карты %s -> %s", card_number, masked)
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта.
    Показывает только последние 4 цифры.
    """
    if len(account_number) < 4 or not account_number.isdigit():
        logger.error("Некорректный номер счёта: %s", account_number)
        raise ValueError("Некорректный номер счёта")

    masked = f"**{account_number[-4:]}"
    logger.debug("Маскирование счёта %s -> %s", account_number, masked)
    return masked
