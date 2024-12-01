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
distance = 0
for id1,id2 in zip(list1,list2):
    distance += abs(int(id1)-int(id2))
print(distance)