import eulerutils as eu

allcount = 0
for n in range(1,100):
    maxns = 10**n
    nthpower = 0
    nthpowers = []
    count=1
    while nthpower<maxns:
        nthpower = count**n
        if eu.number.num_digits(nthpower) == n:
            print("{} digit number {} is an {}^{} power".format(n,nthpower,count,n))
            allcount+=1
        count+=1

print("There are {} such numbers".format(allcount))