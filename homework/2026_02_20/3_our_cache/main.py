def cache(func):

    storage = {}

    def wrapper(a, b):
        key = (a, b)

        if key in storage:
            print("[Кэш]")
            return storage[key]

        print("[Вычисление]")
        result = func(a, b)
        storage[key] = result
        return result

    return wrapper


@cache
def my_sum(a, b):
    return a + b

def main():
    print(my_sum(3, 5))
    print(my_sum(3, 5))
    print(my_sum(10, 2))
    print(my_sum(3, 5))

if __name__ == '__main__':
    main()




