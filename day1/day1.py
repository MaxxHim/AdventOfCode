from pprint import pprint


def step1():
    with open("input.txt", "r") as f:
        content = f.read().splitlines()
        content = [int(i) for i in content]
    counter = 0
    for x, y in zip(content[:-1], content[1:]):
        if x < y:
            counter += 1
    pprint(counter)


def step2():
    with open("input.txt", "r") as f:
        content = f.read().splitlines()
        content = [int(i) for i in content]
    counter = 0
    for i in range(len(content)):
        j = i + 1
        if j > len(content) - 1:
            break
        # pprint(content[i])
        # pprint(content[i:i + 3])
        sum_i = sum(content[i:i + 3])
        # pprint(content[j])
        # pprint(content[j:j + 3])
        sum_j = sum(content[j:j + 3])
        if sum_i < sum_j:
            counter += 1
        else:
            continue
    pprint(counter)


if __name__ == '__main__':
    # step1()
    step2()
