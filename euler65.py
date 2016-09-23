import eulerutils as eu
from fractions import Fraction


# the first item is the value before the semi-colon
# the next items are the ones after the semi-colon
# sqrt2 = [1;(2)]
sqrt2list = (1, 2)
elist = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10]
for i in range(12, 101, 2):
    elist.append(1)
    elist.append(1)
    elist.append(i)
print("Len of elist is {}".format(len(elist)))
#etuple = (2, 1, 2, 1, 1, 4, 1, 1, 6, 1)
#etuple = (2, 1, 2, 1, 1, 4, 1, 1, 6, 1)
fractionlist = elist
print(fractionlist)
#print("Convergent 1 is {}".format(fractionlist[0]))
for a in range(1,101):
    print(fractionlist[1:a])
    frac = eu.convergent.nth_convergent(a, fractionlist)
    #frac =  fractionlist[0] + continued_fraction(fractionlist[1:a])
    # frac = before_semi + recurse_after_semi(nth_convergent, after_semi_list, len(after_semi_list))
    numerator = frac.numerator
    denominator = frac.denominator
    numerator_sum_digits = eu.number.sum_digits(numerator)
    print("Convergent {} is {}/{} - sum of numerator str_digits is {}".format(a , numerator, denominator, numerator_sum_digits))
