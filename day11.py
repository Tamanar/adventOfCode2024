import time

SumLine = 0


def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.split(" ")
    line = [int(x) for x in documentsplit]
    blinkingRange = 75
    lenTotal = search(line, 0, blinkingRange)
    print(f"Result final = {SumLine}")


def search(line, blinkingStart, blinkingRange):
    global SumLine
    lenTotal = len(line)
    for blinking in range(blinkingStart, blinkingRange):
        print(f"{blinking+1}/{blinkingRange}")
        newLine = []
        startTime = time.time()
        for element in line:
            if element == 0:
                newLine.append(1)
            elif len(str(element)) % 2 == 0:
                elementOne = int(str(element)[: int(len(str(element)) / 2)])
                elementTwo = int(str(element)[int(len(str(element)) / 2) :])
                newLine.append(elementOne)
                newLine.append(elementTwo)
            else:
                newLine.append(element * 2024)
        if len(newLine) >= 100000:
            line = newLine[: int(len(newLine) / 2)]
            lenTotal = search(
                newLine[int(len(newLine) / 2) :], blinking + 1, blinkingRange
            )
        else:
            line = newLine[:]
    SumLine += len(line)
    return lenTotal


if __name__ == "__main__":
    main()
    total = 228668
