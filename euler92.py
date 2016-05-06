
def square_of_digits(n):
    strn = str(n)
    total = 0
    for strdig in strn:
        dig = int(strdig)
        total += dig*dig
    return total

size = 10000000
onesSet = set()
eightninesSet = set()
onesSet.add(1)
eightninesSet.add(89)
ones = 0
eightnines = 0
for i in range(1,size):
    if i % 10000 == 0:
        print("{}th ten thousand".format(i//10000))
    chain = []
    chainval = i
    while True:
        chain.append(chainval)
        if chainval in onesSet:
            ones += 1
            for c in chain:
                onesSet.add(c)
            break
        if chainval in eightninesSet:
            eightnines += 1
            for c in chain:
                eightninesSet.add(c)
            break
        chainval = square_of_digits(chainval)

print("There are {} of 89 and {} of 1 and they sum to {}".format(eightnines,ones,eightnines+ones))
