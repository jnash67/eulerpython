import eulerutils as eu
import itertools
import sortedcontainers as sc

sizeOfSetToFind = 114
nums = list(range(2,2*sizeOfSetToFind+1))
minvalofsetnum = 2 *sizeOfSetToFind + 1
#nums = sorted(eu.number.factors(2 * sizeOfSetToFind))
# remove 1 from list
#del[nums[0]]
uniqueminsetsum = sc.SortedSet()
minsetsumdict = sc.SortedDict()

maxfacts = 0
numwithmost = 0
for i in range(2, 24000):
    numfacts = len(eu.number.factors(i))
    print("{} has {} factors".format(i, numfacts ))
    if numfacts > maxfacts:
        maxfacts = numfacts
        numwithmost = i

print("{} has most factors --> {}".format(numwithmost, maxfacts ))


for choose in range(2,15):
    for trialwithoutones in itertools.combinations_with_replacement(nums, choose):
        trialprod = eu.number.product(trialwithoutones)
        # if trialprod == i we can turn trialsum into i by adding 1s without changing trialprod
        if trialprod >= sizeOfSetToFind and trialprod<minvalofsetnum:
            trialsumwithoutones = sum(trialwithoutones)
            # we need prod - sum ones to make the sum and the prod equal
            k = choose + max(0,(trialprod-trialsumwithoutones))
            if k == sizeOfSetToFind:
                minvalofsetnum = trialprod
                setofminval = trialwithoutones
                print("A new lowest set of size {} sums to {} ---> {}".format(sizeOfSetToFind, trialprod, trialwithoutones))
                uniqueminsetsum.add(trialprod)
                minsetsumdict[sizeOfSetToFind]=trialwithoutones
