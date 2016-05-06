import eulerutils as eu
import math
import re


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


oddcount = 0
maxperiod = 0
numwithmaxperiod = 0
largestnuminperiod = 0
numwithlargestnuminperiod = 0
for n in range(1, 10001):
    # for n in range(2,101):
    integer_part = int(math.sqrt(n))
    first_integer_part = integer_part
    aftersemicolonintegerparts = []
    numerator = 1
    addend_in_denominator = -1 * integer_part
    # print("sqrt(n)=[{};(".format(integer_part),end='')
    perfectsquare = False
    # largest period is 217 so we need a couple of multiples of that at least
    # to spot the pattern
    for i in range(0, 1000):
        # Now invert --> i.e. take one over the sqrt(n) + added in denom and "simplify"
        # multiply by (sqrt(n) + (-1* addend)) / (sqrt(n) + (-1* addend))
        # n - int^2
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

    if (not perfectsquare):
        lrs = longest_repeating_list(aftersemicolonintegerparts)
        period = len(lrs)
        maxinlrs = max(lrs)
        if (maxinlrs > largestnuminperiod):
            largestnuminperiod = maxinlrs
            numwithlargestnuminperiod = n
        if (period > maxperiod):
            maxperiod = period
            numwithmaxperiod = n
        if not (period % 2 == 0):
            oddcount += 1
        print("sqrt({})=[{};({})], period={}".format(n, first_integer_part, ",".join(map(str, lrs)), period))
    else:
        period = 0

        # print("{} {}".format(n,period))

print("The total odd count is {}".format(oddcount))
print("The max period is {} for {}".format(maxperiod, numwithmaxperiod))
print("The largest number in a period is {} for {}".format(largestnuminperiod, numwithlargestnuminperiod))
# print(longest_common_substring(patternstring))
