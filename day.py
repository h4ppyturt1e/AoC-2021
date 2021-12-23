def solvePartA(data):
    pass


def solvePartB(data):
    pass


if __name__ == '__main__':
    with open('dayX.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    print(solvePartA(data))
    print(solvePartB(data))