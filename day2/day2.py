from pprint import pprint


def step1():
    with open("input.txt", "r") as f:
        content = f.read().splitlines()
    pprint(content)


if __name__ == '__main__':
    step1()
