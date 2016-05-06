import itertools

# here we have pandigitals that use 0-9
def is10DigitPandigital(numstr):
    resultSet = set()
    noduplicates = True
    for char in numstr:
        digChar = int(char)
        if digChar in resultSet:
            noduplicates = False
        else:
            resultSet.add(digChar)
    if noduplicates:
        return True
    return False

# test="1406357289"
# check = is10DigitPandigital(test)
# if (check):
#     print("YES it is")
# else:
#     print("We have a problem")

sum = 0
count = 0
digitsSet = {0,1,2,3,4,5,6,7,8,9}
for i in itertools.permutations(digitsSet,10):
    d1 = i[0]
    d2 = i[1]
    d3 = i[2]
    d4 = i[3]
    d5 = i[4]
    d6 = i[5]
    d7 = i[6]
    d8 = i[7]
    d9 = i[8]
    d10 = i[9]

    d2d3d4 = d2*100+d3*10+d4
    d3d4d5 = d3*100+d4*10+d5
    d4d5d6 = d4*100+d5*10+d6
    d5d6d7 = d5*100+d6*10+d7
    d6d7d8 = d6*100+d7*10+d8
    d7d8d9 = d7*100+d8*10+d9
    d8d9d10= d8*100+d9*10+d10

    if (d2d3d4 % 2 ==0):
        if (d3d4d5 % 3 ==0):
            if (d4d5d6 % 5 ==0):
                if (d5d6d7 % 7 == 0):
                    if (d6d7d8 % 11 ==0):
                        if (d7d8d9 %13 == 0):
                            if (d8d9d10 % 17 == 0):
                                strnum = ""
                                for n in i:
                                    strnum = strnum + str(n)
                                val = int(strnum)
                                #bingo
                                print("{} is such a 10-digit pandigital with sub-string divisibility".format(strnum))
                                count+=1
                                sum+=val

print("Count of all such pandigitals {}".format(count))
print("Sum of all such pandigitals {}".format(sum))