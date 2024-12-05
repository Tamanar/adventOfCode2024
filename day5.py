from math import floor

listBonne = []


def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    listOrdering = []
    for listNumber in documentsplit:
        listOrdering.append(
            [int(listNumber.split("|")[0]), int(listNumber.split("|")[1])]
        )
    print(listOrdering)
    plouf(listOrdering)


def plouf(listOrdering):
    with open("input2.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    pageOrdering = [x.split(",") for x in documentsplit]
    print(pageOrdering)
    middleSum = 0
    wronglistMiddle = []
    for page in pageOrdering:
        counter = 0
        for pageIndex in range(1, len(page)):
            if not (
                FoundPage(int(page[pageIndex - 1]), int(page[pageIndex]), listOrdering)
            ):
                wronglistMiddle.append(page)
                break
            numberInMiddle = page[floor(len(page) / 2)]
            # listMiddle.append[numberInMiddle]
            # print(numberInMiddle)
            counter += 1

        print(counter)
        if counter == len(page) - 1:
            middleSum += int(numberInMiddle)
    for listWrong in wronglistMiddle:
        (correctList(listWrong, listOrdering, 0))
    global listBonne
    middleSum = 0
    for listInListBonne in listBonne:
        numberInMiddle = listInListBonne[floor(len(listInListBonne) / 2)]
        middleSum += int(numberInMiddle)
    print(middleSum)
    # print(wronglistMiddle)


def correctList(wronglist, listOrdering, depth):
    copyList = wronglist[:]
    newList = []
    listcorrected = False
    global listBonne
    try:
        for pageIndex in range(1, len(wronglist)):
            if not (
                FoundPage(
                    int(wronglist[pageIndex - 1]),
                    int(wronglist[pageIndex]),
                    listOrdering,
                )
            ):
                numberFront = copyList.pop(pageIndex)
                NumberBack = copyList.pop(pageIndex - 1)
                newList = (
                    wronglist[: pageIndex - 1]
                    + [numberFront]
                    + [NumberBack]
                    + wronglist[pageIndex + 1 :]
                )
                wronglist = newList[:]
                listcorrected, listauPif = correctList(newList, listOrdering, depth + 1)
                print(newList)
                listBonne.append(newList)
                # print(listcorrected)
                # print(depth)
                if listcorrected:
                    # print(newList)
                    return False
                    # pass
                else:
                    return False
                # return True
            else:
                listcorrected = True
        return True, newList
    except:
        pass
    # print(listcorrected)
    # return newList


def FoundPage(pagePrevious, PageCurrent, listOrdering):
    listWithPage = []
    for order in listOrdering:
        if pagePrevious in order:
            listWithPage.append(order)
    for orderWithPage in listWithPage:
        if PageCurrent in orderWithPage:
            if PageCurrent == orderWithPage[1]:
                return True

    return False


if __name__ == "__main__":
    main()
