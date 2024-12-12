maxLine = 0
maxcol = 0
ListPosToSkip = []


def main():
    global maxLine
    global maxcol
    global ListPosToSkip
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    listPos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    maxLine = len(documentsplit)
    maxcol = len(documentsplit[0])
    sumTotal = 0
    for lineIndex in range(len(documentsplit)):
        for colIndex in range(len(documentsplit[lineIndex])):
            areaSearch, perimetreSearch = 0, 0

            perimetre = 0
            area = 0
            CurrentChar = documentsplit[lineIndex][colIndex]
            coordonate = [lineIndex, colIndex]
            if coordonate in ListPosToSkip:
                continue
            else:
                area += 1
            for position in listPos:
                newPosLine = lineIndex + position[0]
                newPosCol = colIndex + position[1]
                if not (0 <= newPosLine < maxLine and 0 <= newPosCol < maxcol):
                    perimetre += 1
                elif documentsplit[newPosLine][newPosCol] != CurrentChar:
                    perimetre += 1
                elif documentsplit[newPosLine][newPosCol] == CurrentChar:
                    if coordonate in ListPosToSkip:
                        continue
                    ListPosToSkip.append(coordonate)
                    ListPosToSkip.append([newPosLine, newPosCol])
                    area += 1
                    posToSearch = listPos[:]
                    PosToRemove = [-position[0], -position[1]]
                    posToSearch.remove(PosToRemove)
                    areaSearch, perimetreSearch = search_area(
                        newPosLine,
                        newPosCol,
                        posToSearch,
                        area,
                        0,
                        CurrentChar,
                        documentsplit,
                    )
                # print(
                #    CurrentChar,
                #    areaSearch,
                #    area,
                #    perimetreSearch,
                #    perimetre,
                #    perimetre + perimetreSearch,
                # )
            print(
                f"Char={CurrentChar} As={areaSearch} a={area} Ps={perimetreSearch} p={perimetre}"
            )
            total = (perimetreSearch + perimetre) * areaSearch
            print(total)
            sumTotal += total
            if area == 1:
                print(
                    CurrentChar,
                    area,
                    4,
                )
                total = 4 * 1
                print(total)
                sumTotal += total

    print(sumTotal)


def search_area(
    posLine, posCol, MvtListMinusOne, area, peri, CurrentChar, documentsplit
):
    global maxLine
    global maxcol
    global ListPosToSkip
    listPos = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for position in MvtListMinusOne:
        newPosLine = posLine + position[0]
        newPosCol = posCol + position[1]
        coordonate = [newPosLine, newPosCol]
        if not (0 <= newPosLine < maxLine and 0 <= newPosCol < maxcol):
            peri += 1
        elif documentsplit[newPosLine][newPosCol] != CurrentChar:
            peri += 1
        elif documentsplit[newPosLine][newPosCol] == CurrentChar:
            if coordonate in ListPosToSkip:
                continue
            ListPosToSkip.append([newPosLine, newPosCol])
            area += 1
            posToSearch = listPos[:]
            PosToRemove = [-position[0], -position[1]]
            posToSearch.remove(PosToRemove)
            area, peri = search_area(
                newPosLine,
                newPosCol,
                posToSearch,
                area,
                peri,
                CurrentChar,
                documentsplit,
            )
    return area, peri


if __name__ == "__main__":
    main()
