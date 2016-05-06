import eulerutils as eu
from fractions import Fraction

def continued_fraction(n):
    global resultsDict
    if (n in resultsDict):
        return resultsDict[n]
    if n>0:
        resultsDict[n] = 1/(2+continued_fraction(n-1))
        return resultsDict[n]

count = 0
resultsDict = {}
resultsDict[0] = Fraction(1/2)
for a in range(1,1000):
    frac = 1+continued_fraction(a)
    numerator = frac.numerator
    denominator = frac.denominator
    numerator_digits = eu.number.num_digits(numerator)
    denominator_digits = eu.number.num_digits(denominator)
    if (numerator_digits > denominator_digits):
        count+=1
        print("In the {}th expansion we get {} / {}".format(a+1,numerator, denominator))

print("The count is {}".format(count))
