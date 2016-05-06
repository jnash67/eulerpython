import math
import itertools
import sortedcontainers as sc

# Answer is the the 1912th triangular as the diff 5482660
# pentagonals 1020 and 2167 which are 1560090 and 7042750 have pentagonal sums and differences

# find the minimum diff of pentagonals that is also pentagonal whose sum is also pentagonal
# Iterate through each pentagonal and, for that pentagonal, see if we can find
# two pentagonals for which it is a difference.
# The difference pentagonal has to be in between the lower and higher
# Some algebra shows that the sum can only be found in a range of pentagonals from the difference pentagonal
# in the range diff index - sqrt(higher index) to diff index + sqrt(higher index)
# Not a super tight bound but should be good enough to reduce search space
pentagonals = sc.SortedList()
#for i in range(1,10000000):
maxn = 100000
for i in range(1,maxn):
    pentagonals.append(int(i*(3*i-1)/2))

# pentagonals 1 and 2
lower = pentagonals[0:2]
# pentagonals 4 and 5
higher = pentagonals[3:5]
highestPInHigherList = 5
for mindiffi in range(3,maxn):
    # start of with pentagonal 3 in between lower and higher
    diff = pentagonals[mindiffi-1]
    print("We're on the {}th triangular as the diff {}".format(mindiffi,diff))
    while (higher[-1]/diff < 2.0):
        higher.append(pentagonals[highestPInHigherList])
        highestPInHigherList += 1
        #print("diff between highest {} and second highest {} = {} vs diff {}".format(higher[-1],higher[-2],higher[-1]-higher[-2],diff))

    #higher = pentagonals[mindiffi:mindiffi+maxindexrangeofdiff]
    #print("Actual range is {} - {} for diff of {}. Calculated range was {}".format(l,h,h-l,maxindexrangeofdiff))
    #print("Extra range removed was {}".format(2*maxindexrangeofdiff-(h-l)))

    for p1 in lower:
        for p2 in higher:
            checkdiff = p2-p1
            if (checkdiff == diff):
                sum = p1+p2
                if sum in pentagonals:
                    j = pentagonals.index(p1)+1
                    k = pentagonals.index(p2)+1
                    print("pentagonals {} and {} which are {} and {} have pentagonal sums and differences".format(j,k,p1,p2))
                    print("first to print is the minimum difference is {}".format(diff))
    lower.append(diff)
    del(higher[0])



        # check rolling slice of diff in either direction
    # find index of lowest to check
    # find index of highest to check
    #l = 1
    # for l in range(mindiffi-2,1,-1):
    #     print("pentagonals[l] {} vs diff {}".format(pentagonals[l],diff))
    #     #print("l is {} diff is {} pentagonals[l] is {}".format(l,diff,pentagonals[l]))
    #     if (pentagonals[l]-diff)>=0:
    #         print("l is {} pentagonal[l] is {} diff is {}".format(l,pentagonals[l],diff))
    #         break
    # diff can't be less than half the highest pentagonal we check
    # for h in range(mindiffi, maxn):
    #     if (pentagonals[h] - diff > diff):
    #         break