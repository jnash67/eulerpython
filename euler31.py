import itertools

onep = [1]*200
twop = [2]*100
fivep = [5]*40
tenp = [10]*20
twentyp = [20]*10
fiftyp = [50]*4
onepound = [100]*2
twopound = [200]

change = []
# change.extend(onep)
# change.extend(twop)
# change.extend(fivep)
change.extend(tenp)
change.extend(twentyp)
change.extend(fiftyp)
change.extend(onepound)
change.extend(twopound)
print("Total number of coins " + str(len(change)))

ways = set()
for i in range(1,201):
    print("i is {}".format(i))
    for subset in itertools.combinations(change, i):
        if (sum(subset)==200):
            prevLen = len(ways)
            ways.add(subset)
            lenways = len(ways)
            if (prevLen!=lenways):
                print("subset that works is {}".format(subset))
                print("There are " + str(lenways) + " unique ways")

waysCount = len(ways)
print(ways)
print("There are " + str(waysCount) + " ways to make the change")