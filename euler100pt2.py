from fractions import Fraction


def prob_of_two_blue(blue, red):
    total = blue + red
    prob_b1 = Fraction(blue, total)
    prob_b2 = Fraction(blue - 1, total - 1)
    return prob_b1 * prob_b2


'''
(B/(B+R)) * (B-1/(B+R-1)) = 1/2
B^2 -B - R + 2RB - R^2 = 0
This link solves such 2 variable Diophantine Equations
https://www.alpertron.com.ar/QUAD.HTM

Solution is:
Xn+1 = 1*Xn+2*Yn+0
Yn+1 = 2*Xn+5*Yn-1
X0 =0, Y0 = 0
or
X0 =1 and Y0=1
'''

trillion = 10 ** 12
xn = 1
yn = 0
n = 0
print("for n={}, {} blue and {} red for {} total".format(n, xn, yn, xn + yn))
while True:
    xnplus1 = 1 * xn + 2 * yn + 0
    ynplus1 = 2 * xn + 5 * yn - 1
    xn = xnplus1
    yn = ynplus1
    n += 1
    print("for n={}, {} blue and {} red for {} total".format(n, xn, yn, xn + yn))
    if xn + yn > trillion:
        break

"""
Not exactly sure why but the right answer is X17 = 756872327473 and Y16 = 313506783024
Not sure why it isn't X17 and Y17.  Still, X17, Y16 results in exactly 1/2
"""
print("for n={}, {} blue and {} red for {} total".format(n, xn, yn, xn + yn))
print("{} blue and {} red for {} total".format(xn, yn - xn, yn))

print(prob_of_two_blue(756872327473, 313506783024))
print(prob_of_two_blue(756872327473,313506783023))
print(665857 / 3880899)
print(1070379110497/2140758220990)
print(156753391512 / 1827251437969)
print(756872327473 + 1070379110496)
print(756872327473 + 1827251437969)
