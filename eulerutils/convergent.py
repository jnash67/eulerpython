import math
from fractions import Fraction


# utilities related to continued fractions

# the first item is the value before the semi-colon
# the next items are the ones after the semi-colon
# e.g. sqrt(23) = [4;(1,3,1,8)]
def nth_convergent(n, full_list):
    # assume it's an infinitely repeating representation
    lenlist = len(full_list)
    if (n < lenlist):
        after_semi_list = full_list[1:n]
    else:
        after_semi_list = full_list[1:lenlist]
    if n > lenlist:
        # duplicate
        mult = (n // (lenlist - 1)) + 1
        after_semi_list = after_semi_list * mult
        after_semi_list = after_semi_list[0:n - 1]

    return full_list[0] + continued_fraction(after_semi_list)


def continued_fraction(after_semi_list):
    n = len(after_semi_list)
    if n == 0:
        return Fraction(0)
    if n == 1:
        return 1 / Fraction(after_semi_list[0])
    if n > 1:
        # pass the list minus the last element
        first_elem = after_semi_list[0]
        recurse_result = continued_fraction(after_semi_list[1:len(after_semi_list)])

        return 1 / (first_elem + recurse_result)


def longest_repeating_list(list):
    listlen = len(list)
    for i in range(1, listlen + 1):
        sublist = list[0:i]
        maxpossible = int(listlen / i)
        multipleofsublists = list[0:i * maxpossible]
        # we want non-overlapping substrings
        found = True
        for check in range(0, maxpossible):
            frag = multipleofsublists[check * i:(check + 1) * i]
            for item in range(0, i):
                if not (frag[item] == sublist[item]):
                    found = False
                    break
        if found:
            return sublist


def period_of_convergent_fraction_representation_of_sqrt(list):
    return len(list) - 1


# largest period is 217 for N<=10,000 so we need a couple of multiples of that at least
# to spot the pattern
# Tested for num<=10000
def convergent_fraction_representation_of_sqrt(n):
    assert (n <= 10000,
            "This may not work for this num.  The largest period for num<=10k is 217.  Need to be sure we have a long enough string to find the pattern.")

    integer_part = int(math.sqrt(n))
    first_integer_part = integer_part
    aftersemicolonintegerparts = []
    numerator = 1
    addend_in_denominator = -1 * integer_part
    # print("sqrt(num)=[{};(".format(integer_part),end='')
    perfectsquare = False
    # go for a long time until we're sure we've duplicated the repeating
    for i in range(0, 1000):
        # Now invert --> i.e. take one over the sqrt(num) + added in denom and "simplify"
        # multiply by (sqrt(num) + (-1* addend)) / (sqrt(num) + (-1* addend))
        # num - int^2
        new_denom_without_square_root = n - (addend_in_denominator ** 2)
        if (new_denom_without_square_root == 0):
            # perfect square
            perfectsquare = True
            break
        new_addend_in_numerator_with_square_root = -1 * addend_in_denominator
        integer_part = int(
            numerator * (math.sqrt(n) + new_addend_in_numerator_with_square_root) / new_denom_without_square_root)
        # now subtract the new integer part from the fraction
        new_denom_without_square_root = int(new_denom_without_square_root / numerator)
        new_addend_in_numerator_with_square_root = new_addend_in_numerator_with_square_root - \
                                                   integer_part * new_denom_without_square_root

        aftersemicolonintegerparts.append(integer_part)

        # prepare for inverting
        addend_in_denominator = new_addend_in_numerator_with_square_root
        numerator = new_denom_without_square_root
        # print(longest_unique_substr(patternstring))

    result_list = [first_integer_part]
    if not perfectsquare:
        lrs = longest_repeating_list(aftersemicolonintegerparts)
        for ip in lrs:
            result_list.append(ip)
    return result_list
