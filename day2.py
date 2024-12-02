with open("day2input.txt", "r") as f:
    all_document = f.read()
documentplit = all_document.splitlines()

list1 = []


def safe(listToTest: list) -> bool:
    unsafe = True
    lastNumber = lineInt[0]
    if lineInt[1] - lineInt[0] > 0:
        IsIncreasing = True
    else:
        IsIncreasing = False
    for number in lineInt[1:]:

        if lastNumber == number:
            unsafe = False
            break
        diff = abs(lastNumber - number)
        if not (1 <= diff <= 3):
            unsafe = False
            break
        if (number - lastNumber > 0) != IsIncreasing:
            unsafe = False
            break
        lastNumber = number
    return unsafe


unsafe = 0
for line in documentplit:
    lineInt = [int(stringInList) for stringInList in line.split(" ")]
    if not (safe(lineInt)):
        unsafe += 1
print(len(documentplit) - unsafe)
