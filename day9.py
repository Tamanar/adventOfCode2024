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
            for numberOfData in range(int(zipData)):
                unzip_list.append(counter)
            counter += 1
            isFile = False
        else:
            for numberOfPoint in range(int(zipData)):
                unzip_list.append(".")
            isFile = True
    return unzip_list


def rearrange(unzip_list):
    for index in range(len(unzip_list)):
        if unzip_list[index] == ".":
            for indexInverse in range(len(unzip_list) - 1, -1, -1):
                if indexInverse < index:
                    break
                else:
                    if unzip_list[indexInverse] != ".":
                        unzip_list[index], unzip_list[indexInverse] = (
                            unzip_list[indexInverse],
                            unzip_list[index],
                        )
                        break
    return unzip_list


def check_sum(listRearrange):
    checkSum = 0
    for index in range(len(listRearrange)):
        if listRearrange[index] == ".":
            break
        else:
            checkSum += index * listRearrange[index]
    return checkSum


if __name__ == "__main__":
    main()
