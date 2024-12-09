import operator

ops = {"+": operator.add, "*": operator.sub}


def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))


def main(ops):

    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    dico = {}
    for line in documentsplit:
        resultValue = line.split(":")
        dico[int(resultValue[0])] = resultValue[1].split(" ")[1:]
    somme = 0
    for key, values in dico.items():
        listBin = []
        result = 0
        nbrOperator = len(values) - 1
        for index in range(pow(3, nbrOperator)):
            listBin.append(((ternary(index))))
        maxSize = len(listBin[-1])
        for stringBinaryIndex in range(len(listBin)):
            stringBinary = listBin[stringBinaryIndex]
            while len(stringBinary) < maxSize:
                stringBinary = "0" + stringBinary
            listBin[stringBinaryIndex] = stringBinary

        for AlloperatorPossibity in listBin:
            result = int(values[0])
            for operator in range(len(AlloperatorPossibity)):
                if AlloperatorPossibity[operator] == "0":
                    result += int(values[operator + 1])
                elif AlloperatorPossibity[operator] == "1":
                    result *= int(values[operator + 1])
                else:
                    result = int(str(result) + values[operator + 1])
            if result == key:
                print(key)
                somme += key
                break

    print(somme)


if __name__ == "__main__":
    main(ops)
