def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    continue
                except OSError:
                    print(f"{func.__name__} raise OSError exception.")
                    continue
            return None
        return wrapper
    return decorator
