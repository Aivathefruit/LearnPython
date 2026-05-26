def bread(func):
    def wrapper():
        print("Bread")
        func()
        print("Bread")
    return wrapper

def salat(func):
    def wrapper():
        print("Salat")
        func()
    return wrapper

def tomato(func):
    def wrapper():
        print("Tomato")
        func()
    return wrapper

def cheese(func):
    def wrapper():
        print("Cheese")
        func()
    return wrapper

def meat(func):
    def wrapper():
        print("Meat")
        func()
    return wrapper

def pickle(func):
    def wrapper():
        print("Pickle")
        func()
    return wrapper

@bread
@salat
@pickle
@tomato
@cheese
@meat
def make_sandwich():
    pass

def main():
    make_sandwich()

if __name__ == '__main__':
    main()
