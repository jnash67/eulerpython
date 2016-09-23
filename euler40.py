import math

def num_digits(n):
    d = int(math.log10(n))+1
    return d

def nth_pos_of_number(num, n):
    strval = str(num)
    strdig = strval[n]
    print(strdig)
    return int(strdig)

runningPos = 0
digitList = []
for i in range(1,1000000):
    d = num_digits(i)
    if (runningPos<1) and (runningPos+d>=1):
        n = 1-runningPos-1
        d1 = nth_pos_of_number(i,n)
        digitList.append(d1)
    elif (runningPos<10) and (runningPos+d>=10):
        n = 10-runningPos-1
        d10 = nth_pos_of_number(i,n)
        digitList.append(d10)
    elif (runningPos<100) and (runningPos+d>=100):
        n = 100-runningPos-1
        d100 = nth_pos_of_number(i,n)
        digitList.append(d100)
    elif (runningPos<1000) and (runningPos+d>=1000):
        n = 1000-runningPos-1
        d1000 = nth_pos_of_number(i,n)
        digitList.append(d1000)
    elif (runningPos<10000) and (runningPos+d>=10000):
        n = 10000-runningPos-1
        d10000 = nth_pos_of_number(i,n)
        digitList.append(d10000)
    elif (runningPos<100000) and (runningPos+d>=100000):
        n = 100000-runningPos-1
        d100000 = nth_pos_of_number(i,n)
        digitList.append(d100000)
    elif (runningPos<1000000) and (runningPos+d>=1000000):
        n = 1000000-runningPos-1
        d1000000 = nth_pos_of_number(i,n)
        digitList.append(d1000000)
    runningPos = runningPos + d

mult = 1
for i in digitList:
    mult = mult * i

print(digitList)
print("The mult of the str_digits is {}".format(mult))
