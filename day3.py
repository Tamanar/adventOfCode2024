def detect(string: str):
    SOMMME = 0
    listMul = string.split("mul(")
    print(listMul)
    for stringInList in listMul:
        listMulSplitWithPar = stringInList.split(")")
        whereItShouldBe = listMulSplitWithPar[0]
        splitWithVirgule = whereItShouldBe.split(",")
        try:
            number1 = int(splitWithVirgule[0])
            number2 = int(splitWithVirgule[1])
            SOMMME += multiple(number1, number2)
        except:
            continue
    return SOMMME


def multiple(number1, number2):
    return number1 * number2


def main():
    with open("day3input.txt", "r") as f:
        all_document = f.read()
    print(detect(all_document))


if __name__ == "__main__":
    main()
