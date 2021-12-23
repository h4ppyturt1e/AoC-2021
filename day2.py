def solvePartA(data):
    horizPos, depth = 0, 0
    for instruction, value in data:
        value = int(value)
        if instruction == "forward":
            horizPos += value
        elif instruction == "down":
            depth += value
        elif instruction == "up":
            depth -= value
    return horizPos * depth

def solvePartB(data):
    horizPos, depth, aim = 0, 0, 0
    for instruction, value in data:
        value = int(value)
        if instruction == "forward":
            horizPos += value
            depth += aim * value
        elif instruction == "down":
            aim += value
        elif instruction == "up":
            aim -= value
    return horizPos * depth


if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        data = [tuple(line.strip().split()) for line in f.readlines()]
    print(solvePartA(data))
    print(solvePartB(data))