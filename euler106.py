# import eulerutils as eu
import itertools


# Here we don't need to have an actual special sum set.  We need a set of size n where all
# values are strictly increasing.  We can just assume that all subsets of unequal size
# follow rule 2.  We just need to see how many comparisons we would need to do to check for compliance
# with rule 1 that equal size subsets don't have the same sums.  For this, we don't care what the
# specific values are, just that they're strictly increasing.  If two subsets have the same size and
# the values of the one don't all come from the beginning of the special set and the values of the other
# don't all come from later then a check is needed.

# For a given n, we want to iterate through all pairs of disjoint subsets of equal size 1..n-1

def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def subsets_of_size(iterable, n):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, n))


def all_disjoint_pairs_of_equal_size(strictly_increasing_set):
    for r in range(1, len(strictly_increasing_set) + 1):
        for pair in itertools.combinations(subsets_of_size(strictly_increasing_set, r), 2):
            p1 = pair[0]
            p2 = pair[1]
            if is_empty(p1 - p2):
                print("disjoint sets {} {}".format(p1, p2))


def count_comparisons(n):
    all_disjoint_pairs_of_equal_size(range(1, n + 1))


# n = 4 optimum special set candidate found (3, 5, 6, 7) with len 21
# n = 5 optimum special set candidate found (6, 9, 11, 12, 13) with len 51
# n = 6 optimum special set candidate found (11, 17, 20, 22, 23, 24) with len 117
# n = 7 optimum special set candidate found (11, 18, 19, 20, 22, 25) with len 115
# n = 8 optimum special set candidate found (20, 31, 38, 39, 40, 42, 45) with len 255
count_comparisons(4)