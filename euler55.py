import eulerutils as eu

count = 0
for i in range(10,10000):
    numToTest = i
    lychrel = True
    for j in range(0,50):
        numToTest = numToTest + eu.numtext.reverse_num(numToTest)
        if (eu.numtext.is_palindrome(numToTest)):
            lychrel = False
            break
    if lychrel:
        count+=1
        print("{} is lychrel for purposes of this exercise".format(i))
print("There are {} lychrels under 10000".format(count))