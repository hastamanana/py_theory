from file_09_02 import say_hello
from figures import circle_area
from figures.circle import circle_area


def main(name: str) -> None:
    print(say_hello(name))


if __name__ == '__main__':
    main(input())
