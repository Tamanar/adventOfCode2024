import time
def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    grid = all_document.splitlines()
    for rowIndex in range(len(grid)):
        grid[rowIndex] = list(grid[rowIndex])
    with open("input2.txt", "r") as f:
        all_document = f.read()
    allMovement = all_document
    for rowIndex in range(len(grid)):
        for colIndex in range (len(grid[0])):
            if grid[rowIndex][colIndex] == "@":
                posInit = [rowIndex,colIndex]
                posRow = rowIndex
                posCol = colIndex
    print(allMovement)
    print(posInit)
    for move in allMovement:
        if move == "<":
            newPosRow = posRow
            newPosCol = posCol - 1
            movement = [0,-1]
        elif move == ">":
            newPosRow = posRow
            newPosCol = posCol + 1
            movement = [0,1]
        elif move == "v":
            newPosRow = posRow + 1
            newPosCol = posCol 
            movement = [1,0]
        elif move == "^":
            newPosRow = posRow - 1
            newPosCol = posCol 
            movement = [-1,0]
        if grid[newPosRow][newPosCol] == "#":
            continue
        elif grid[newPosRow][newPosCol] == ".":
            grid[newPosRow][newPosCol] = "@"
            grid[posRow][posCol] = "."
            posCol,posRow = newPosCol,newPosRow
            continue
        elif grid[newPosRow][newPosCol] == "O":
            canPush = checkCanPush(newPosRow,newPosCol,movement,grid)
            if canPush:
                grid[newPosRow][newPosCol] = "@"
                grid[posRow][posCol] = "."
                posCol,posRow = newPosCol,newPosRow
                continue
    SumGPS = 0
    for row in grid:
        print(row)
    for rowIndex in range(len(grid)):
        for colIndex in range (len(grid[0])):
            if grid[rowIndex][colIndex] == "O":
                print(rowIndex,colIndex)
                GPS = 100 *rowIndex + colIndex
                SumGPS += GPS
    print(SumGPS)
def checkCanPush (posRowToCheck,posColToCheck,movement,grid):
    newPosRow = posRowToCheck + movement[0]
    newPosCol = posColToCheck + movement[1]
    if grid[newPosRow][newPosCol] == ".":
        grid[newPosRow][newPosCol] = "O"
        grid[posRowToCheck][posColToCheck] = "."
        return True
    elif grid[newPosRow][newPosCol] == "#":
        return False
    if grid[newPosRow][newPosCol] == "O":
        CanPush = checkCanPush(newPosRow,newPosCol,movement,grid)
        if CanPush:
            grid[newPosRow][newPosCol] = "O"
            grid[posRowToCheck][posColToCheck] = "."
            return True
        else:
            return CanPush
            


if __name__ == "__main__":
    main()
