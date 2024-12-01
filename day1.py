with open("day1input1.txt","r") as f:
    all_document = f.read()
documentplit = all_document.splitlines()
list1 = []
list2 = []
for line in documentplit:
    list1.append(line.split(" ")[0])
    list2.append(line.split(" ")[-1])
list1.sort()
list2.sort()
similiarities = 0
for id1 in list1:
    score = list2.count(id1) * int(id1)
    if score > 0:
        similiarities += score
        print(id1)
print(similiarities)