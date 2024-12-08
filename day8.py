def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    print(documentsplit)
    allListAntipode = []
    for coordY in range(len(documentsplit)):
        for coordX in range(len(documentsplit[coordY])):
            char  = documentsplit[coordY][coordX]
            if char!= ".":
                allListAntipode += search_similar(coordY,coordX,char,documentsplit)
    print(len(allListAntipode))
    print((allListAntipode))
    cleanList = cleanAntipode(allListAntipode,len(documentsplit),len(documentsplit[0]))
    print((cleanList))
    print(len(cleanList))
def search_similar(coordYIn,coordXIn,charIn,documentsplit) ->list:
    listAntipode = []
    for coordY in range(len(documentsplit)):
        for coordX in range(len(documentsplit[coordY])):
            char  = documentsplit[coordY][coordX]
            if char == charIn:
                if not(coordY==coordYIn and coordX==coordXIn):
                    antipodepos = [coordY+(coordY-coordYIn),coordX+(coordX-coordXIn)]
                    listAntipode.append(antipodepos)

    return listAntipode
def cleanAntipode (listAllAntipode:list,maxX,maxY):
    cleanListOut = []
    for antipodePos in listAllAntipode:
        if (0<=antipodePos[0]<maxY and 0<=antipodePos[1]<maxX):
            cleanListOut.append(antipodePos)
    cleanList = []
    for antipodePosIndex in range(len(cleanListOut)):
        if not(cleanListOut[antipodePosIndex] in cleanListOut[antipodePosIndex+1:]) :
            cleanList.append(cleanListOut[antipodePosIndex])
    return cleanList
if __name__ == "__main__":
    main()
