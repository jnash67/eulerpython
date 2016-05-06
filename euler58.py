import eulerutils as eu

# print(eu.spiral.create_clockwise_spiral(5))
# print
# print(eu.spiral.create_counterclockwise_spiral(5))
# print(eu.spiral.new_counterclockwise_spiral_diagonals(5))
# print(eu.spiral.new_counterclockwise_spiral_diagonals(7))

# maxn = 90000000
# # we use primes for primality testing so it should contain all primes below the max
# primes = eu.primes.all_primes_between(2,maxn)
# print("There are {} primes".format(len(primes)))
# biggestprime = primes[len(primes)-1]

below10pct = False
spiralSize = 7
countPrimes = 8
totalCount = 13
while not below10pct:
    spiralSize += 2
    diags = eu.spiral.new_counterclockwise_spiral_diagonals(spiralSize)
    for p in diags:
        if (eu.primes.is_prime(p)):
            countPrimes +=1
        totalCount+=1
    ratio = countPrimes / totalCount
    assert totalCount == 2*spiralSize -1, "Look into this"
    print("For spiral size {} there are {} primes out of {} for ratio of {}".format(spiralSize,countPrimes, 2*spiralSize-1, ratio))
    if ratio < .1:
        below10pct = True