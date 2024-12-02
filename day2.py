with open("day2input.txt", "r") as f:
    all_document = f.read()
documentplit = all_document.splitlines()

list1 = []


def safe(listToTest: list, profondeur) -> bool:
    if profondeur > 1:
        return False
    profondeur += 1
    unsafe = True
    lastNumber = listToTest[0]
    if listToTest[1] - listToTest[0] > 0:
        IsIncreasing = True
    else:
        IsIncreasing = False
    index = 0
    for number in listToTest[1:]:

        if lastNumber == number:
            unsafe = (
                safe(listToTest[:index] + listToTest[index + 1 :], profondeur)
                or safe(listToTest[: index - 1] + listToTest[index:], profondeur)
                or safe(listToTest[: index + 1] + listToTest[index + 2 :], profondeur)
            )
            break
        diff = abs(lastNumber - number)
        if not (1 <= diff <= 3):
            unsafe = (
                safe(listToTest[:index] + listToTest[index + 1 :], profondeur)
                or safe(listToTest[: index - 1] + listToTest[index:], profondeur)
                or safe(listToTest[: index + 1] + listToTest[index + 2 :], profondeur)
            )
            break
        if (number - lastNumber > 0) != IsIncreasing:
            unsafe = (
                safe(listToTest[:index] + listToTest[index + 1 :], profondeur)
                or safe(listToTest[: index - 1] + listToTest[index:], profondeur)
                or safe(listToTest[: index + 1] + listToTest[index + 2 :], profondeur)
            )
            break
        lastNumber = number
        index += 1
    return unsafe


unsafe = 0
for line in documentplit:
    lineInt = [int(stringInList) for stringInList in line.split(" ")]
    if not (safe(lineInt, 0)):
        unsafe += 1
print(len(documentplit) - unsafe)
