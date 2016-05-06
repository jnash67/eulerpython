

digitFactorials = [1,1,2,6,24,120,720,5040,40320,362880]

sumOfAll=0
for i in range(3,10000000):
    stri = str(i)
    sumOfFacts = 0
    for char in stri:
        dig = int(char)
        sumOfFacts += digitFactorials[dig]
    if (i == sumOfFacts):
        print("{} is curious".format(i))
        sumOfAll += i

print("sum of all curious is {}".format(sumOfAll))