import eulerutils as eu

maxn = 1000000
found = False
for i in range(1,maxn):
    if (i % 10000 == 0):
        print("We're on # {}".format(i))
    if (eu.numtext.same_digits_and_same_length(i, 2*i)):
        if (eu.numtext.same_digits_and_same_length(2*i, 3*i)):
            if (eu.numtext.same_digits_and_same_length(3*i, 4*i)):
                if (eu.numtext.same_digits_and_same_length(4*i, 5*i)):
                    if (eu.numtext.same_digits_and_same_length(5*i, 6*i)):
                        print("The first positive integer is {}".format(i))
                        break