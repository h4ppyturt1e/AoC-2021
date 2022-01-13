def parse(data):
    bingoNums = data[0].split(",")
    boards = []
    
    curBoard = []
    for line in data[1:]:
        if line != "":
            curBoard.append([[i, False] for i in line.split()])
        if len(curBoard) == 5:
            boards.append(curBoard)
            curBoard = []
            
    # print(bingoNums)
    # print(boards)
    
    return bingoNums, boards


def markNumber(board, num):
    for i in range(5):
        for j in range(5):
            # print(i, j)
            if board[i][j][0] == num:
                board[i][j][1] = True
                # print(board[i][j])
    # print("done")
    return board


def checkBoard(board):
    """ 
    00, 01, 02, 03, 04
    10, 11, 12, 13, 14
    20, 21, 22, 23, 24
    30, 31, 32, 33, 34
    40, 41, 42, 43, 44
    
    00, 10, 20, 30, 40
    01, 11, 21, 31, 41
    02, 12, 22, 32, 42
    03, 13, 23, 33, 43
    04, 14, 24, 34, 44
    """
    # checks with respect to i
    for line in board:
        allTrue = all([x[1] for x in line])
        if allTrue:
            return True
    # checks with respect to j
    transposedBoard = list(zip(*board))
    for line in transposedBoard:
        # print(line)
        allTrue = all([x[1] for x in line])
        if allTrue:
            return True
    return False


def solvePartA(bingoNums, boards):
    lastBINGO = -1
    BINGOboard = None
    
    for curBingo in bingoNums:
        for boardIndex in range(len(boards)):
            boards[boardIndex] = markNumber(boards[boardIndex], curBingo)
            if checkBoard(boards[boardIndex]):
                lastBINGO = curBingo
                BINGOboard = boards[boardIndex]
                break
        if lastBINGO != -1:
            break
    
    uncheckedNums = []    
    for i in range(5):
        for j in range(5):
            if BINGOboard[i][j][1] == False:
                uncheckedNums.append(BINGOboard[i][j][0])

    # print(uncheckedNums)

    # gets product of all unchecked numbers
    uncheckedSum = 0
    for num in uncheckedNums:
        uncheckedSum += int(num)
    # print(uncheckedSum)
    
    
    return uncheckedSum * int(lastBINGO)


def solvePartB(data):
    return


if __name__ == '__main__':
    with open('day4.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
        
    bingoNums, boards = parse(data)
    
    print(solvePartA(bingoNums, boards))
    print(solvePartB(data))