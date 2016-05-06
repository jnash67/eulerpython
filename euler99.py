import math

file = "p099_base_exp.txt"
expTupleList = []
for line in list(open(file)):
    line = line.strip()
    print(line)
    listOfStr = line.split(",")
    num = int(listOfStr[0])
    exp = int(listOfStr[1])
    expTupleList.append((num, exp))

numLines = len(expTupleList)
print("Number of lines is {}".format(numLines))

maxSoFar = 0
maxTuple = ()
countOfMaxSoFar = 0
for i in range(0, numLines, 1):
    num = expTupleList[i][0]
    exp = expTupleList[i][1]
    calc = exp * math.log(num)
    if calc > maxSoFar:
        maxSoFar = calc
        countOfMaxSoFar = i+1
        maxTuple = (num, exp)

print("The max is on line {} with tuple {}".format(countOfMaxSoFar, maxTuple))