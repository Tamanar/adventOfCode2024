def main():
    with open("input.txt") as f:
        all_document = f.read()
    documentplit = all_document.splitlines()
    detection(documentplit)


def detection(listString: list):
    numberOfDetection = 0
    for indexcolone in range(len(listString)):
        for indexLine in range(len(listString[indexcolone])):
            if listString[indexcolone][indexLine] == "M":
                try:
                    if directionToSearch(
                        [1, -1], "A", indexcolone, indexLine, listString
                    ) and (
                        directionToSearch(
                            [1, 1], "M", indexcolone, indexLine - 2, listString
                        )
                        or directionToSearch(
                            [-1, -1], "M", indexcolone + 2, indexLine, listString
                        )
                    ):
                        print([1, -1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [1, 1], "A", indexcolone, indexLine, listString
                    ) and (
                        directionToSearch(
                            [-1, 1], "M", indexcolone + 2, indexLine, listString
                        )
                        or directionToSearch(
                            [-1, -1], "M", indexcolone, indexLine + 2, listString
                        )
                    ):
                        print([1, 1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [-1, 1], "A", indexcolone, indexLine, listString
                    ) and (
                        directionToSearch(
                            [-1, -1], "M", indexcolone, indexLine + 2, listString
                        )
                        or directionToSearch(
                            [1, 1], "M", indexcolone - 2, indexLine, listString
                        )
                    ):
                        print([-1, 1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
                try:
                    if directionToSearch(
                        [-1, -1], "A", indexcolone, indexLine, listString
                    ) and (
                        directionToSearch(
                            [1, -1], "M", indexcolone - 2, indexLine, listString
                        )
                        or directionToSearch(
                            [-1, 1], "M", indexcolone, indexLine - 2, listString
                        )
                    ):
                        print([-1, -1], indexcolone, indexLine)
                        numberOfDetection += 1
                except:
                    pass
    print(numberOfDetection)


def directionToSearch(direction: list, letter, indexcolone, indexline, liststring):
    FindTheLetter = False
    if 0 <= indexcolone < len(liststring) and 0 <= indexline < len(
        liststring[indexcolone]
    ):

        # Validate the next position
        next_row = indexcolone + direction[0]
        next_col = indexline + direction[1]
        if next_row < 0 or next_col < 0:
            return False
        newLetter = liststring[next_col][
            next_row
        ]  # Debug print to understand the letter matching
        print(f"Searching for {letter}, found {newLetter} at ({next_row}, {next_col})")
        if 0 <= next_row < len(liststring) and 0 <= next_col < len(
            liststring[next_row]
        ):
            if newLetter == letter:
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
