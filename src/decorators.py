from functools import wraps
from typing import Any, Callable, Optional
import sys


def log(filename: Optional[str] = None):
    """
    Декоратор для логирования работы функций.

    :param filename: путь к файлу логов (если None — вывод в консоль).
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message, file=sys.stdout)

                return result

            except Exception as e:
                message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message, file=sys.stdout)

                raise
        return wrapper
    return decorator
