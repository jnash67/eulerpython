
resultsDict = {}
for p in range(1,1001):
    # Let a always be the smaller of a,b.  Otherwise we will get
    # double results of a,b and b,a.
    for a in range(1,1001):
        if (a > p):
            break
        for b in range(a,1001):
            if (a+b>p):
                break
            # c is always bigger than b (c^2 = b^2 + a^2)
            for c in range(max(b,p-a-b),1001):
                left = a**2+b**2
                csq = c**2
                sum=a+b+c
                if (sum>p) or (left>csq):
                    break
                if (left==csq) and (sum==p):
                    # found a solution for p. increment dictionary counter.
                    resultsDict[p] = resultsDict.get(p,0) + 1
                    print("For p {} we have [{},{},{}]".format(p,a,b,c))
                    print("Dict now has {} values for p {}".format(resultsDict[p],p))

print(resultsDict)
print("The p with the highest value is {}".format(max(resultsDict, key=resultsDict.get)))