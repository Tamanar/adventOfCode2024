def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.split(" ")
    line = [int(x) for x in documentsplit]
    blinkingRange = 25
    for blinking in range(blinkingRange):
        print(f"{blinking+1}/{blinkingRange}")
        print(f"current len = {len(line)}")
        newLine = []
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
        line = newLine[:]
    print(f"total length = {len(line)}")


if __name__ == "__main__":
    main()
