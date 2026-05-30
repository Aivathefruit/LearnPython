def cache(func):

    storage = {}

    def wrapper(*args):
        if args in storage:
            print("[Кэш]")
            return storage[args]

        print("[Вычисление]")
        result = func(*args)
        storage[args] = result
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




