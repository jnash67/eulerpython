import eulerutils as eu
import itertools
import sortedcontainers as sc


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

uniquesums = sc.SortedSet()
r = 4

for i in range(1, 5):
    for j in itertools.combinations(i,r):
        uniquesums.clear()
        found = False
        for sub in powerset(i):
            subsum = sum(sub)
            if subsum in uniquesums:
                found = True
                break
            else:
                uniquesums.add(subsum)
         if found:

             print("")


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
