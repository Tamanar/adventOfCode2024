from math import floor


def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    print(documentsplit)
    cleanDoc = [x for x in documentsplit if x != ""]
    ListPrize = []
    for index in range(0, len(cleanDoc), 3):
        print(index)
        for smallIndex in range(3):
            print(index + smallIndex)
            print(cleanDoc[index + smallIndex])
            if "A" in cleanDoc[index + smallIndex]:
                print(cleanDoc[index + smallIndex].split("+"))
                Xa = cleanDoc[index + smallIndex].split("+")[1][:2]
                Ya = cleanDoc[index + smallIndex].split("+")[-1][:2]
                A = [int(Xa), int(Ya)]
                print(A)
            if "B" in cleanDoc[index + smallIndex]:
                print(cleanDoc[index + smallIndex].split("+"))
                Xb = cleanDoc[index + smallIndex].split("+")[1][:2]
                Yb = cleanDoc[index + smallIndex].split("+")[-1][:2]
                B = [int(Xb), int(Yb)]
                print(B)
            if "z" in cleanDoc[index + smallIndex]:
                print(cleanDoc[index + smallIndex].split("="))
                Yprize = cleanDoc[index + smallIndex].split("=")[-1]
                Xprize = cleanDoc[index + smallIndex].split("=")[1].split(",")[0]
                Prize = [int(Xprize) + 10000000000000, int(Yprize) + 10000000000000]
                print(Prize)
        ListPrize.append([A, B, Prize])
    print(ListPrize)
    sumToken = 0
    for element in ListPrize:
        print(element)
        sumToken += calculate(element[0], element[1], element[2])
    print(sumToken)


def calculate(A, B, Prize):
    PrizeX = Prize[0]
    PrizeY = Prize[1]
    Ax = A[0]
    Ay = A[1]
    Bx = B[0]
    By = B[1]
    token = 0
    # bestToSearchX = min(floor(PrizeX / Ax), floor(PrizeX / Bx))
    # bestToSearchY = min(floor(PrizeY / Ay), floor(PrizeY / By))
    bestToSearchX = floor(PrizeX / Ax)
    # print(bestToSearchX)
    # print(bestToSearchY)
    for PushButtonA in range(bestToSearchX, -1, -1):

        tryEquation = PrizeX - (Ax * PushButtonA)
        PushButtonB = tryEquation / Bx
        print(PushButtonA)
        if PushButtonB % 1 == 0.0:
            # print(f"tryEquation = {tryEquation}")
            # print(f"PushButtonA = {PushButtonA}")
            # print(f"PushButtonB= {PushButtonB}")
            if (PushButtonA * Ax + PushButtonB * Bx == PrizeX) and (
                PushButtonA * Ay + PushButtonB * By == PrizeY
            ):
                print("find")
                token = PushButtonA * 3 + PushButtonB * 1
                break
    return token


if __name__ == "__main__":
    main()
