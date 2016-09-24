import eulerutils as eu

maxdigitsum = 0
for a in range(1,100):
    for b in range(1,100):
        r = a**b
        sumofdigits = eu.number.sum_digits(r)
        if sumofdigits > maxdigitsum:
            maxdigitsum = sumofdigits
            print("sum of digits {} results from {}^{} = {}".format(sumofdigits,a,b,r))

print("The maximum digital sum is {}".format(maxdigitsum))