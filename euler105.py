# import eulerutils as eu
import itertools


# Unlike for 103 where the point was to find the "optimum" special sum set, the point here
# is to determine whether a each set in a list of sets is a special sum set
# (i.e. meets all the conditions), optimal or not

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

file = "p105_sets.txt"

s = 0
total_sum = 0
for line in list(open(file)):
    line = line.strip()
    set_list = set(map(int, line.split(",")))
    set_sum = sum(set_list)
    if test_special_sum_set(set_list, set_sum +1 ) == set_sum:
        print("{} is special sum set".format(set_list))
        total_sum += set_sum

print("Total is {}".format(total_sum))