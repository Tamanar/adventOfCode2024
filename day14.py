def main():
    with open("input.txt", "r") as f:
        all_document = f.read()
    documentsplit = all_document.splitlines()
    listRobot=[]
    secondeMax = 100
    wide = 11
    tall = 7
    dot_grid = [['.' for _ in range(wide+1)] for _ in range(tall+1)]


    for element in documentsplit:
        elementCut = element.split(" ")
        postoGet = elementCut[0]
        velocityToGet = elementCut[1]
        posY = postoGet.split(",")[-1]
        veloY = velocityToGet.split(",")[-1]
        posX=postoGet.split(",")[0].split("=")[-1]
        veloX=velocityToGet.split(",")[0].split("=")[-1]
        robot = [[int(posX),int(posY)],[int(veloX),int(veloY)]]
        listRobot.append(robot)
    print(listRobot)
    for robot in listRobot:
        posX=robot[0][0]
        posY=robot[0][1]
        vX=robot[1][0]
        vY=robot[1][1]
        for seconds in range(secondeMax):
            newPosX = posX + vX
            newPosY = posY + vY
            if newPosX < 0:
                newPosX = wide + newPosX
            elif newPosX >= wide:
                newPosX = newPosX - wide
            if newPosY < 0:
                newPosY = tall + newPosY
            elif newPosY >= tall:
                newPosY = newPosY - tall
            posX = newPosX
            posY = newPosY
        robot[0][0]=posX
        robot[0][1]=posY
    print(listRobot)
    halfX = wide //2
    halfY = tall //2
    quadran1 = 0
    quadran2 = 0
    quadran3 = 0
    quadran4 = 0
        # Print the grid to visualize it
    for robot in listRobot:
        posX=robot[0][0]
        posY=robot[0][1]
        if dot_grid[posY][posX] == '.':
            dot_grid[posY][posX] = 1
        else:
            dot_grid[posY][posX] +=1
    for row in dot_grid:
        print(row)
    for robot in listRobot:
        posX=robot[0][0]
        posY=robot[0][1]
        print(posX,posY)
        if 0<=posX<halfX and 0<=posY<halfY:
            quadran1+=1
        elif halfX<posX<wide and 0<=posY<halfY:
            quadran2+=1
        elif 0<=posX<halfX and halfY<posY<tall:
            quadran3+=1
        elif halfX<posX<wide and halfY<posY<tall:
            quadran4+=1
    print(quadran1,quadran2,quadran3,quadran4)
    print(quadran1*quadran2*quadran3*quadran4)
if __name__ == "__main__":
    main()
