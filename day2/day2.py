from pprint import pprint


def step1():
    with open("input.txt", "r") as f:
        content = f.read().splitlines()
    # pprint(content)
    content = [elem.split() for elem in content]
    # pprint(content)
    horizontal = 0
    depth = 0
    for command, number in content:
        if command == 'forward':
            horizontal += int(number)
        elif command == 'down':
            depth += int(number)
        elif command == 'up':
            depth -= int(number)
        else:
            raise Exception("something wrong !")
    return horizontal, depth


def step2():
    with open("input.txt", "r") as f:
        content = f.read().splitlines()
    content = [elem.split() for elem in content]
    horizontal = 0
    depth = 0
    aim = 0
    for command, number in content:
        if command == 'forward':
            horizontal += int(number)
            depth += int(number) * aim
        elif command == 'down':
            aim += int(number)
        elif command == 'up':
            aim -= int(number)
        else:
            raise Exception("something wrong !")
    return horizontal, depth


if __name__ == '__main__':
    ln = '\n'
    horizontal, depth = step1()
    print(f"step 1 : " + "\n" +
          f"- horizontal = {horizontal}"
          f"- depth = {depth}")
    horizontal, depth = step2()
    print(f"step 2 : {ln}- horizontal = {horizontal}{ln}- depth = {depth}")
