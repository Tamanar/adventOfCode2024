def main():
    with open("input.txt", "r") as f:
        all_document = f.read()

    unzip = create_space(all_document)
    print(unzip)
    rearrangeList = rearrange(unzip)
    print(rearrangeList)
    checkSum = check_sum(rearrangeList)
    print(checkSum)


def create_space(line):
    unzip_list = []
    counter = 0
    isFile = True
    for zipData in line:
        if isFile:
            strConcat = ""
            for numberOfData in range(int(zipData)):
                strConcat += str(counter)
            unzip_list.append((strConcat))
            counter += 1
            isFile = False
        else:
            strConcat = ""
            for numberOfPoint in range(int(zipData)):
                strConcat += "."
            if strConcat != "":
                unzip_list.append(strConcat)
            isFile = True
    return unzip_list


def rearrange(unzip_list: list):
    for index in range(len(unzip_list)):
        print(f"{index}/{len(unzip_list)}")
        if "." in unzip_list[index]:
            for indexInverse in range(len(unzip_list) - 1, -1, -1):
                if indexInverse < index:
                    break
                else:

                    if not ("." in unzip_list[indexInverse]):
                        if len(unzip_list[index]) >= len(str(unzip_list[indexInverse])):
                            partToCut = unzip_list[index][
                                : len(str(unzip_list[indexInverse]))
                            ]
                            partToKeep = unzip_list[index][
                                len(str(unzip_list[indexInverse])) :
                            ]
                            unzip_list.pop(index)
                            # unzip_list.insert(index, unzip_list[indexInverse])
                            unzip_list.insert(index, unzip_list[indexInverse - 1])
                            unzip_list.insert(index + 1, partToKeep)
                            unzip_list.pop(indexInverse + 1)
                            unzip_list.insert(indexInverse + 1, partToCut)
                            break
            # for indexUnzip_list in range(len(unzip_list)):
            #    try:
            #        if (
            #            "." in unzip_list[indexUnzip_list + 1]
            #            and "." in unzip_list[indexUnzip_list]
            #        ):
            #            dotPlusOne = unzip_list.pop(indexUnzip_list + 1)
            #            unzip_list[indexUnzip_list] += dotPlusOne
            #    except:
            #        break
    rearrangeList = []
    for thing in unzip_list:
        if thing != "":
            rearrangeList.append(thing)
    return rearrangeList


def check_sum(listRearrange):
    checkSum = 0
    counter = 0
    for numberOrString in listRearrange:
        if not ("." in numberOrString):
            for number in range(len(str(numberOrString))):
                checkSum += counter * int(str(numberOrString)[0])
                counter += 1
        else:
            for sizeDot in numberOrString:
                counter += 1
    return checkSum


if __name__ == "__main__":
    main()
