def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentplit = all_document.splitlines()
    detection(documentplit)


def detection(listString: list):
    numberOfDetection = 0
    for indexcolone in range(len(listString)):
        for indexLine in range(len(listString[indexcolone])):
            if listString[indexcolone][indexLine] == "X":
                try:
                    if directionToSearch(
                        [0, 1], "M", indexcolone, indexLine, listString
                    ):
                        print([0, 1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [0, -1], "M", indexcolone, indexLine, listString
                    ):
                        print([0, -1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [1, -1], "M", indexcolone, indexLine, listString
                    ):
                        print([1, -1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [1, 1], "M", indexcolone, indexLine, listString
                    ):
                        print([1, 1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [-1, 1], "M", indexcolone, indexLine, listString
                    ):
                        print([-1, 1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [-1, -1], "M", indexcolone, indexLine, listString
                    ):
                        print([-1, -1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [-1, 0], "M", indexcolone, indexLine, listString
                    ):
                        print([-1, 0], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [1, 0], "M", indexcolone, indexLine, listString
                    ):
                        print([1, 0], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
    print(numberOfDetection)


def directionToSearch(direction: list, letter, indexcolone, indexline, liststring):
    FindTheLetter = False
    if 0 <= indexcolone + direction[0] < len(liststring) and 0 <= indexline + direction[
        1
    ] < len(liststring[indexcolone]):
        if liststring[indexcolone + direction[0]][indexline + direction[1]] == letter:
            if letter == "M":
                FindTheLetter = directionToSearch(
                    direction,
                    "A",
                    indexcolone + direction[0],
                    indexline + direction[1],
                    liststring,
                )
            elif letter == "A":
                FindTheLetter = directionToSearch(
                    direction,
                    "S",
                    indexcolone + direction[0],
                    indexline + direction[1],
                    liststring,
                )
            elif letter == "S":
                FindTheLetter = True
    return FindTheLetter


if __name__ == "__main__":
    main()
