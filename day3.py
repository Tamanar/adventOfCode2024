def detectString(string: str):
    SOMMME = 0
    listMulCutWithDont = string.split("don't()")
    for listDont in listMulCutWithDont:
        listDo = listDont.split("do()")
        # print(listDo)
        for StringDoDO in listDo[1:]:
            SOMMME += detectMul(StringDoDO.split("mul("))
    SOMMME += detectMul(listMulCutWithDont[0].split("mul("))

    return SOMMME


def detectMul(stringSo: str):
    print(stringSo)
    SOMMME = 0
    for stringInList in stringSo:
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
    print(detectString(all_document))


if __name__ == "__main__":
    main()
