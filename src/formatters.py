from typing import Any, Dict

from src.widget import mask_account_card  # или: from src.widget import mask_account_card
from src.widget import get_date


def _safe_mask(value: Any) -> str:
    """
    Безопасно маскирует значение, если это строка с номером карты/счёта.
    Если маскирование бросило ошибку — возвращаем исходную строку.
    """
    if not value or not isinstance(value, str):
        return ""
    try:
        return mask_account_card(value)
    except Exception:
        # Если mask_account_card может выбрасывать ValueError для коротких номеров,
        # лучше вернуть оригинальную строку (или пустую), чтобы программа не падала.
        return value


def format_amount(operation_amount: Dict[str, Any]) -> str:
    """
    Формирует строку суммы для печати.
    Поддерживает структуру operationAmount: {"amount": "...", "currency": {"code": "RUB", "name": "руб."}}
    """
    if not operation_amount:
        return "Сумма: -"
    amount = operation_amount.get("amount", "")
    currency = operation_amount.get("currency", {})
    code = ""
    if isinstance(currency, dict):
        code = (currency.get("code") or currency.get("name") or "").strip()
    code_up = (code or "").upper()
    if code_up in ("RUB", "РУБ", "РУБ."):
        return f"Сумма: {amount} руб."
    if code_up == "":
        return f"Сумма: {amount}"
    return f"Сумма: {amount} {code_up}"


def format_transaction(tx: Dict[str, Any]) -> str:
    """
    Возвращает многострочный форматированный блок с информацией по транзакции.
    Пример:
    11.03.2024 Открытие вклада
    Счет **4321
    Сумма: 40542 руб.
    """
    date_str = get_date(tx.get("date", ""))  # безопасно форматируем дату
    desc = tx.get("description", "").strip()

    from_raw = tx.get("from") or tx.get("source") or ""
    to_raw = tx.get("to") or tx.get("destination") or ""

    from_mask = _safe_mask(from_raw)
    to_mask = _safe_mask(to_raw)

    # Строка вида "A -> B" или одна сторона, если другой нет
    transfer_line = ""
    if from_mask and to_mask:
        transfer_line = f"{from_mask} -> {to_mask}"
    elif from_mask:
        transfer_line = f"{from_mask}"
    elif to_mask:
        transfer_line = f"{to_mask}"
    else:
        # если нет полей from/to, оставим пустую строку
        transfer_line = ""

    amount_line = format_amount(tx.get("operationAmount", {}))

    parts = []
    # первая строка: дата + описание
    header = f"{date_str} {desc}".strip()
    parts.append(header)
    if transfer_line:
        parts.append(transfer_line)
    parts.append(amount_line)

    return "\n".join(parts)
