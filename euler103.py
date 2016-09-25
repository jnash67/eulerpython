import itertools


# The point of this problem is to find "optimum" special sum sets.  The "optimum" is the
# set that meets all the criteria AND the sum of the elements is the minimum.

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def test_special_sum_set(sss, lowest_found):
    sum_of_sss = sum(sss)
    if sum_of_sss >= lowest_found:
        # no need to continue
        return lowest_found
    found = True
    for subset in powerset(sss):
        subset_len = len(subset)
        if subset_len > 0:
            sum_of_subset = sum(subset)
            disjoint_vals = set(sss) - set(subset)
            for disjoint_subset in powerset(disjoint_vals):
                disjoint_len = len(disjoint_subset)
                if disjoint_len > 0:
                    sum_of_disjoint = sum(disjoint_subset)
                    if sum_of_disjoint == sum_of_subset:
                        # sums of subsets cannot be equal
                        found = False
                        break
                    if disjoint_len > subset_len:
                        if not (sum_of_disjoint > sum_of_subset):
                            found = False
                            break
                    if subset_len > disjoint_len:
                        if not (sum_of_subset > sum_of_disjoint):
                            found = False
                            break
        if not found:
            break
    if found:
        print("optimum special set candidate found {} with len {}".format(sss, sum_of_sss))
        return sum_of_sss
    return lowest_found


def special_sum_set(n, middle_val_of_prev_sss, highest_val_of_prev_sss, prev_optimum_special_sum):
    minval = middle_val_of_prev_sss
    maxval = highest_val_of_prev_sss + middle_val_of_prev_sss + 1
    possible_vals = set(range(minval, maxval + 1))
    # according to problem, good estimate of "near" optimum sum
    lowest_found = prev_optimum_special_sum + n*middle_val_of_prev_sss + 1
    for possible_sss in itertools.combinations(possible_vals, n):
        lowest_found = test_special_sum_set(possible_sss, lowest_found)


# num = 4 optimum special set candidate found (3, 5, 6, 7) with len 21
# num = 5 optimum special set candidate found (6, 9, 11, 12, 13) with len 51
# num = 6 optimum special set candidate found (11, 17, 20, 22, 23, 24) with len 117
# num = 7 optimum special set candidate found (11, 18, 19, 20, 22, 25) with len 115
# num = 8 optimum special set candidate found (20, 31, 38, 39, 40, 42, 45) with len 255
special_sum_set(4, 3, 4, 9)
special_sum_set(5, 6, 7, 21)
special_sum_set(6, 11, 13, 51)
special_sum_set(7, 20, 25, 115)