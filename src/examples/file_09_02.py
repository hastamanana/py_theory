def say_hello(name: str) -> str:
    return f'Привет, {name}'


if __name__ == '__main__':
    print(say_hello('Ivan'))
    print(__name__)
