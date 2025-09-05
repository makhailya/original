from typing import list, dict


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    :param data: список словарей с транзакциями
    :param state: статус для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, отфильтрованный по указанному статусу
    """
    return [item for item in data if item.get("state") == state]


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
]

print(filter_by_state(transactions))
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

print(filter_by_state(transactions, "CANCELED"))
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """
    Сортирует список словарей по ключу 'date'.
    :param data: список словарей с транзакциями
    :param descending: порядок сортировки (по умолчанию True — убывание)
    :return: новый список словарей, отсортированный по дате
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=descending)


print(sort_by_date(transactions))
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

print(sort_by_date(transactions, descending=False))
# [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
