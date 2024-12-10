counterNine = 0
posNine = {}


def main():
    global counterNine

    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    for lineIndex in range(len(documentsplit)):
        for colIndex in range(len(documentsplit[lineIndex])):
            if int(documentsplit[lineIndex][colIndex]) == 0:
                searchBehind(documentsplit, lineIndex, colIndex, 0)
                print(len(posNine))
                counterNine += len(posNine)
                posNine.clear()
    print(counterNine)


def searchBehind(doc, posX, posY, step):
    global posNine
    listMvmt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for mvmt in listMvmt:
        newPosX = posX + mvmt[0]
        newPosY = posY + mvmt[1]
        if 0 <= newPosX < len(doc) and 0 <= newPosY < len(doc[0]):
            if int(doc[newPosX][newPosY]) == 9 and step == 8:
                posNine[f"[{newPosX}, {newPosY}]"] = 1
            elif int(doc[newPosX][newPosY]) == step + 1:
                searchBehind(doc, newPosX, newPosY, step + 1)
    return


if __name__ == "__main__":
    main()
