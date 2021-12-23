def solvePartA(data):
    prevNum = data[0]
    total = 0
    for curNum in data[1:]:
        if curNum > prevNum:
            total += 1
        prevNum = curNum
    return total
    

def solvePartB(data):
    threeMeasurementsSums = []
    for i in range(len(data)-2):
        threeMeasurementsSums.append(sum(data[i:i+3]))
    return solvePartA(threeMeasurementsSums)

if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
    print(solvePartA(data))
    print(solvePartB(data))
    