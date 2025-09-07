# Учебный проект по Python
# 📌 Project: Bank Data Processing

## 🎯 Цель проекта

Проект предназначен для обработки банковских данных:
- маскировка номеров карт и счетов;
- фильтрация операций по статусу (`EXECUTED`, `CANCELED` и др.);
- сортировка операций по дате;
- преобразование даты в удобочитаемый формат.

---

## 📂 Описание проекта

Проект включает функции для:
- маскирования номеров карт и счетов;
- форматирования дат;
- фильтрации и сортировки операций по дате и состоянию.

### Модули проекта
- `masks` — маскирование карт и счетов;
- `widget` — работа с данными карт/счетов и форматирование даты;
- `processing` — фильтрация и сортировка операций.

---

## ⚙️ Использование функций

### Маскирование карты
```python
from masks import get_mask_card_number

masked_card = get_mask_card_number("7000792289606361")
print(masked_card)  # 7000 79** **** 6361

---

## ✅ Тестирование

В проекте используется библиотека **pytest** для модульного тестирования.

### Покрытие тестами
Тестами проверяются функции:
- `get_mask_card_number`
- `get_mask_account`
- `mask_account_card`
- `get_date`
- `filter_by_state`
- `sort_by_date`

### Запуск тестов
Установите зависимости:
```bash
pip install -r requirements.txt
---

## 🌀 Generators

В проекте реализован модуль `generators`, содержащий удобные генераторы для работы с транзакциями и номерами карт.

### `filter_by_currency`
Фильтрация транзакций по валюте:
```python
from generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for tx in usd_transactions:
    print(tx)
