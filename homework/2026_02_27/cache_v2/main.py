import json
import os
from functools import wraps


def cache_v2(filename='cache.json', use_args_as_key=True):

    def decorator(func):
        storage = {}

        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    loaded_cache = json.load(f)
                    storage.update(loaded_cache)
            except (json.JSONDecodeError, IOError):
                print(f"Ошибка чтения файла {filename}. Начинаем с пустого кэша.")

        @wraps(func)
        def wrapper(*args, **kwargs):
            if use_args_as_key:
                key = str(args)
            else:
                sorted_kwargs = tuple(sorted(kwargs.items()))
                key = str(sorted_kwargs)

            if key in storage:
                print(f"[Кэш] Значение найдено для ключа {key}")
                return storage[key]

            print(f"[Вычисление] Результат для {key} не найден, вычисляю...")
            result = func(*args, **kwargs)


            try:
                json.dumps(result)
                storage[key] = result
            except TypeError:
                storage[key] = str(result)

            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(storage, f, ensure_ascii=False, indent=4)
            except IOError:
                print(f"Ошибка сохранения в файл {filename}")

            return result

        return wrapper

    return decorator


# --- Пример использования ---

@cache_v2(filename='cache_addition.json', use_args_as_key=True)
def my_sum(a, b):
    return a + b


@cache_v2(filename='cache_multiplication.json', use_args_as_key=False)
def my_multiply(a, b):
    return a * b


def main():
    print("--- Тест 1: Позиционные аргументы (my_sum) ---")
    print(my_sum(3, 5))
    print(my_sum(3, 5))
    print(my_sum(10, 2))

    print("\n--- Тест 2: Именованные аргументы (my_multiply) ---")
    print(my_multiply(b=4, a=4))
    print(my_multiply(a=2, b=4))


if __name__ == '__main__':
    main()
