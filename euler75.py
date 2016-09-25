import math
import eulerutils as eu
import sortedcontainers as sc

# generate pythagorean integer triples a,b,c where a^2 + b^2 = c^2
# and a+b+c == length where there's only 1 a,b,c for a length
# only possible triples are (odd, even, odd), (even, odd, even) or (even, even, even)
# so length can only be even

# this formula generates ALL primitive triples: ( m2 – n2 )2 + (2 m num)2 = ( m2 + n2 )2 for some m and num
# and some but not all non-primitives
# a primitive triple has no common factors


minlength = 12
maxlength = 100
foundLengths = sc.SortedSet()
for length in range(minlength, maxlength + 1, 2):
    if not length in foundLengths:
        c_bound = length // 2 + 1
        upper_bound = int(math.sqrt(c_bound * c_bound / 2)) + 1
        count = 0
        founda = foundb = foundc = 0
        next_length = False
        # lowest a is 3 for (3,4,5)
        for a in range(3, upper_bound+1):
            if next_length:
                break
            asq = a * a
            for b in range(a, upper_bound+1):
                bsq = b * b
                possible_c = length - a - b
                # lowest c is 5 for (3,4,5)
                if possible_c < 5:
                    break
                if asq + bsq == possible_c * possible_c:
                    founda = a
                    foundb = b
                    foundc = possible_c
                    count += 1
                    if count > 1:
                        next_length = True
                        break

        if count == 1:
            foundLengths.add(length)
            print("Found not already checked off ---> {} cm: ({},{},{})".format(length, founda, foundb, foundc))
            for m in range(2, maxlength//length + 1):
                mult = m * length
                if mult > maxlength:
                    break
                foundLengths.add(mult)

print("There are {} values".format(len(foundLengths)))
