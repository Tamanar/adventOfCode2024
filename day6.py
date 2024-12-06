def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    print(documentsplit)
    for coordY in range(len(documentsplit)):
        for coordX in range(len(documentsplit[coordY])):
            if documentsplit[coordY][coordX] == "^":
                CoordGuardX = coordX
                CoordGuardY = coordY
    guard = "^"
    print(CoordGuardX, CoordGuardY)
    sizeMaxX = len(documentsplit[0])
    sizeMaxY = len(documentsplit)
    tableauPost = documentsplit[:]
    posCounter = 0
    while True:
        if not (documentsplit[CoordGuardY][CoordGuardX] == "X"):
            posCounter += 1
        if guard == "^":
            newCoordY = CoordGuardY - 1
            if newCoordY < 0:
                break
            if documentsplit[newCoordY][CoordGuardX] == "#":
                guard = ">"
                posCounter -= 1
            else:
                S = list(tableauPost[CoordGuardY])
                if S[CoordGuardX] == "X":
                    posCounter -= 1
                S[CoordGuardX] = "X"

                tableauPost[CoordGuardY] = S
                CoordGuardY = newCoordY
                if tableauPost[CoordGuardY][CoordGuardX] == "X":
                    posCounter -= 1
                S = list(tableauPost[CoordGuardY])
                S[CoordGuardX] = guard
                tableauPost[CoordGuardY] = S
        elif guard == "v":
            newCoordY = CoordGuardY + 1
            if newCoordY >= sizeMaxY:
                break
            if documentsplit[newCoordY][CoordGuardX] == "#":
                guard = "<"
                posCounter -= 1
            else:
                S = list(tableauPost[CoordGuardY])
                S[CoordGuardX] = "X"
                tableauPost[CoordGuardY] = S
                CoordGuardY = newCoordY
                if tableauPost[CoordGuardY][CoordGuardX] == "X":
                    posCounter -= 1
                S = list(tableauPost[CoordGuardY])
                S[CoordGuardX] = guard
                tableauPost[CoordGuardY] = S
        elif guard == ">":
            newCoordX = CoordGuardX + 1
            if newCoordX >= sizeMaxX:
                break
            if documentsplit[CoordGuardY][newCoordX] == "#":
                guard = "v"
                posCounter -= 1
            else:
                S = list(tableauPost[CoordGuardY])
                S[CoordGuardX] = "X"
                tableauPost[CoordGuardY] = S
                CoordGuardX = newCoordX
                if tableauPost[CoordGuardY][CoordGuardX] == "X":
                    posCounter -= 1
                S = list(tableauPost[CoordGuardY])
                S[CoordGuardX] = guard
                tableauPost[CoordGuardY] = S
        elif guard == "<":
            newCoordX = CoordGuardX - 1
            if newCoordX < 0:
                break
            if documentsplit[CoordGuardY][newCoordX] == "#":
                guard = "^"
                posCounter -= 1
            else:
                S = list(tableauPost[CoordGuardY])
                S[CoordGuardX] = "X"
                tableauPost[CoordGuardY] = S
                CoordGuardX = newCoordX
                if tableauPost[CoordGuardY][CoordGuardX] == "X":
                    posCounter -= 1

                S = list(tableauPost[CoordGuardY])
                S[CoordGuardX] = guard
                tableauPost[CoordGuardY] = S
    print(posCounter)


if __name__ == "__main__":
    main()
