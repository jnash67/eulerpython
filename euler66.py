import eulerutils as eu
from fractions import Fraction

# this diophantine equation (pell's equation) can be solved by
# looking at convergents for continued fraction for sqrt(D)
# x^2 - D y^2 = 1
# The minimizing x1,y1 are the ith convergent hi/ki for some i

maxx = 0
dofmaxx = 0
for D in range(1, 1001):
    fraclist = eu.convergent.convergent_fraction_representation_of_sqrt(D)
    if (len(fraclist)>1):
        # not a perfect square
        solution_found = False
        n = 0
        while not solution_found:
            n += 1
            frac = eu.convergent.nth_convergent(n, fraclist)
            numerator = frac.numerator
            denominator = frac.denominator
            if (numerator**2-D*denominator**2 == 1):
                # we have a minimal solution for D
                solution_found = True
                print("{}^2 - {}*{}^2 = 1".format(numerator, D, denominator))
                if (numerator > maxx):
                    maxx= numerator
                    dofmaxx = D
                    print("We have a new max.  The max value of x is {} for D {}".format(maxx, dofmaxx))


print("The max value of x is {} for D {}".format(maxx, dofmaxx))