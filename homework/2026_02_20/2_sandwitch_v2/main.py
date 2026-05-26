def bread(func):
    def wrapper():
        return f"Bread\n{func()}Bread"
    return wrapper

def salat(func):
    def wrapper():
        return f"Salat\n{func()}"
    return wrapper

def tomato(func):
    def wrapper():
        return f"Tomato\n{func()}"
    return wrapper

def meat(func):
    def wrapper():
        return f"Meat\n{func()}"
    return wrapper

@bread
@salat
@tomato
@meat
def make_sandwich():
    return ''

def main():
    print(make_sandwich())

if __name__ == '__main__':
    main()
