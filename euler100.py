import eulerutils as eu
from fractions import Fraction


def prob_of_two_blue(blue, red):
    total = blue + red
    prob_b1 = Fraction(blue, total)
    prob_b2 = Fraction(blue-1, total-1)
    return prob_b1 * prob_b2


trillion = 10**12
half = Fraction(1/2)
#print(half.numerator / half.denominator)
for b in range(707106781187, 2*trillion):
    for r in range(trillion-b+1, 2*trillion):
        p = prob_of_two_blue(b,r);
        #print("Prob is {} for {} blue and {} red for total {}".format(p.numerator / p.denominator, b, r, b + r))
        if p < half:
            break
        #print("Prob is {} for {} blue and {} red for total {}".format(p.numerator/p.denominator, b, r, b + r))
        if (p == half):
            print("Found for {} blue and {} red for total {}".format(b,r,b+r))
            break




