import eulerutils as eu
import itertools

# Here we don't need to have an actual special sum set.  We need a set of size num where all
# values are strictly increasing.  We can just assume that all subsets of unequal size
# follow rule 2.  We just need to see how many comparisons we would need to do to check for compliance
# with rule 1 that equal size subsets don't have the same sums.  For this, we don't care what the
# specific values are, just that they're strictly increasing.  If two subsets have the same size and
# the values of the one don't all come from the beginning of the special set and the values of the other
# don't all come from later then a check is needed.

# For a given num, we want to iterate through all pairs of disjoint subsets of equal size 1..num-1


def all_disjoint_pairs_of_equal_size(strictly_increasing_set):
    # we know all pairs of size 1 are disjoint since the set is strictly increasing and none of these requiring testing
    set_size = len(strictly_increasing_set)
    possiblePairs = int(eu.number.choose(set_size, 2))
    possibleDisjointPairs = possiblePairs
    testingRequired = 0
    for r in range(2, set_size//2+1):
        subsets = set(eu.subsets.subsets_of_size(strictly_increasing_set, r))
        possiblePairs += int(eu.number.choose(len(subsets), 2))
        for pair in itertools.combinations(subsets,2):
            p1 = list(pair[0])
            p2 = list(pair[1])
            if frozenset(pair[0]).isdisjoint(frozenset(pair[1])):
                possibleDisjointPairs+=1
                # if every corresponding item is later in one than in the other then
                # we don't have to do comparisons.
                numLater = 0
                numEarlier = 0
                for i in range(0,r):
                    i1 = p1[i]
                    i2 = p2[i]
                    if (i1 > i2) :
                        numLater += 1
                    else:
                        numEarlier +=1
                if not(numLater == 0 or numEarlier == 0):
                    #print("disjoint set that needs to be counted {} {}".format(p1, p2))
                    testingRequired+=1
    # Note: My count of equal pairs is different than the problem statement count of possible subsets because
    # these include comparisons of unequal sized pairs as well and sum just disjoint subsets.
    print("{} Subsets require testing out of total {} equal joint and disjoint pairs. A total of {} were disjoint".format(testingRequired, possiblePairs, possibleDisjointPairs))

def count_comparisons(n):
    strictly_increasing_set = set(range(1,n+1))
    all_disjoint_pairs_of_equal_size(strictly_increasing_set)


count_comparisons(4)
count_comparisons(7)
count_comparisons(12)