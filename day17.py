A = 47792830
B = 0
C = 0
outList = []


def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    docuSplit = all_document.split(",")
    pointer = 0
    while pointer < (len(docuSplit)):
        opcode = int(docuSplit[pointer])
        combo = int(docuSplit[pointer + 1])
        if opcode == 0:
            pointer = adv(combo, pointer)
        elif opcode == 1:
            pointer = bxl(combo, pointer)
        elif opcode == 2:
            pointer = bst(combo, pointer)
        elif opcode == 3:
            pointer = jnz(combo, pointer)
        elif opcode == 4:
            pointer = bxc(combo, pointer)
        elif opcode == 5:
            pointer = out(combo, pointer)
        elif opcode == 6:
            pointer = bdv(combo, pointer)
        elif opcode == 7:
            pointer = cdv(combo, pointer)
        if pointer >= len(docuSplit):
            break
    print(outList)


def findOperand(combo):
    global A
    global B
    global C
    if combo == 4:
        return A
    elif combo == 5:
        return B
    elif combo == 6:
        return C
    elif combo < 4:
        return combo


def adv(combo, pointer):
    global A
    denominator = findOperand(combo)
    denominator = pow(2, denominator)
    A = A // denominator
    return pointer + 2


def bdv(combo, pointer):
    global A
    global B
    denominator = findOperand(combo)
    denominator = pow(2, denominator)
    B = A // denominator
    return pointer + 2


def cdv(combo, pointer):
    global A
    global C
    denominator = findOperand(combo)
    denominator = pow(2, denominator)
    C = A // denominator
    return pointer + 2


def bxl(combo, pointer):
    global B
    B = B ^ combo
    return pointer + 2


def bst(combo, pointer):
    global B
    ToModulate = findOperand(combo)
    B = ToModulate % 8
    return pointer + 2


def jnz(combo, pointer):
    if A == 0:
        return pointer + 2
    else:
        return combo


def bxc(combo, pointer):
    global B
    B = B ^ C
    return pointer + 2


def out(combo, pointer):
    ToPrint = findOperand(combo)
    outList.append(ToPrint % 8)
    return pointer + 2


if __name__ == "__main__":
    main()
