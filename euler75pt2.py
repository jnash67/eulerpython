import math
import eulerutils as eu
import itertools
import sortedcontainers as sc
import eulerutils as eu

# generate pythagorean integer triples a,b,c where a^2 + b^2 = c^2
# and a+b+c == length where there's only 1 a,b,c for a length
# only possible triples are (odd, even, odd), (even, odd, even) or (even, even, even)
# so length can only be even

# this formula generates ALL primitive triples: ( m2 – n2 )2 + (2 m num)2 = ( m2 + n2 )2 for some m and num
# and some but not all non-primitives
# a primitive triple has no common factors
# m^2 + num^2 < max length
# if m>num, m < sqrt(max length / 2)

@eu.timing.timeit
def use_math_gcd():
    global lengthsDict
    for m in range(2, size//2):
        for n in range(1, m):
            # m - num has to be odd
            if (m - n) % 2 == 1:
                msq = m * m
                nsq = n * n
                a = msq - nsq
                b = 2 * m * n
                c = msq + nsq
                length = a + b + c
                if length > size:
                    break
                if length <= size:
                    if math.gcd(a, b) == 1 and math.gcd(a, c) == 1 and math.gcd(b, c) == 1:
                        # if eu.primes.is_pythagorean_triple_primitive(a, b, c):
                        # print("Primitive ({},{},{}) --> {}".format(a,b,c,length))
                        mcount = 0
                        for mult in range(length, size + 1, length):
                            mcount += 1
                            # for each primitive and its multiples, add one to the possible ways of generating the length
                            if b > a:
                                # lengthsDict.setdefault(mult, []).append((a, b, c))
                                # primitives.add((a,b,c))
                                lengthsDict.setdefault(mult, []).append((mcount * a, mcount * b, mcount * c))
                            else:
                                # lengthsDict.setdefault(mult, []).append((b, a, c))
                                # primitives.add((b,a,c))
                                lengthsDict.setdefault(mult, []).append((mcount * b, mcount * a, mcount * c))


@eu.timing.timeit
def use_my_own_primitives_function():
    global lengthsDict2
    for m in range(2, size//2):
        for n in range(1, m):
            # m - num has to be odd
            if (m - n) % 2 == 1:
                msq = m * m
                nsq = n * n
                a = msq - nsq
                b = 2 * m * n
                c = msq + nsq
                length = a + b + c
                if length > size:
                    break
                if length <= size:
                    if eu.primes.is_pythagorean_triple_primitive(a, b, c):
                        # print("Primitive ({},{},{}) --> {}".format(a,b,c,length))
                        mcount = 0
                        for mult in range(length, size + 1, length):
                            mcount += 1
                            # for each primitive and its multiples, add one to the possible ways of generating the length
                            if b > a:
                                # lengthsDict.setdefault(mult, []).append((a, b, c))
                                # primitives.add((a,b,c))
                                lengthsDict2.setdefault(mult, set()).add((mcount * a, mcount * b, mcount * c))
                            else:
                                # lengthsDict.setdefault(mult, []).append((b, a, c))
                                # primitives.add((b,a,c))
                                lengthsDict2.setdefault(mult, set()).add((mcount * b, mcount * a, mcount * c))


#size = 2000
#size = 135000
size = 1500000
lengthsDict = sc.SortedDict()
lengthsDict2 = sc.SortedDict()
use_math_gcd()
use_my_own_primitives_function()

count = 0
for key in lengthsDict.keys():
    sols = lengthsDict[key]
    if len(sols) == 1:
        if (len(lengthsDict2[key])!=1):
            print("MISSING IN 2 --> {} {}".format(key, lengthsDict[key]))
            print("{}".format(lengthsDict2[key]))

        #print("Length {} --> {}".format(key, sols))
        count += 1
print("There are {} values for which exactly one integer side right angle triangle can be formed".format(count))
