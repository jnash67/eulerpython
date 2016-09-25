import eulerutils as eu
import sortedcontainers as sc

# Only run this version in Debug mode.  It keeps hanging my system.

# 1/x + 1/y = 1/num ==> xy /(y+x) = num ==> nx + ny = xy
# nx and ny will always have gcd num
# for any num, x = 2*num and y = 2*num is always a solution.  This is the solution where x is largest and y is smallest.
# for any num, x = num+1, y = num*x = num*(num+1) is always a solution.  This is the solution where x is smallest and y is largest.
# num*(num+1) + num*num*(num+1) = (num+num^2)*(num+1) = num*(num^2 + 1) * (num+1)
# max possible solutions is 2*num - num+1, one for each possible x

#nmax = 100000
nstart = 24
nmax = 24
test = [24,78,360,15620,6400,1100,150000]
solutions_to_exceed = 1000
max_count_so_far = 2
for n in test:
    print("\n({}): ".format(n), end="")
    sol_set = set()
    x_set = sc.SortedSet();
    # these are always solutions
    sol_set.add((n+1, n*(n+1)))
    x_set.add(n+1)
    sol_set.add((n*2, n*2))
    x_set.add(n*2)
    count= 2
    # print("({},{}) ".format(num+1, num*(num+1)), end="")
    # print("({},{}) ".format(num*2, num *2), end="")
    pfactors = set(eu.primes.prime_factors(n))
    print("prime factors of num {}".format(pfactors))
    # exclude num+1 and 2*num which we've already added
    for x in range(n+2, n*2):
        y_set = sc.SortedSet()
        for p in pfactors:
            y_set.update(range(x+p,x*x,p))
        for y in y_set:
            xy = x * y
            nx_plus_ny = n * x + n * y
            if xy == nx_plus_ny:
                if not(x in x_set):
                    count+=1
                    sol_set.add((x,y))
                    x_set.add(x)
                    print("({},{}) ".format(x, y), end ="")
            if xy > nx_plus_ny:
                break
    print("\n({}): {}".format(n, count))
    if count> max_count_so_far:
        max_count_so_far = count
        print("Max count so far {}".format(max_count_so_far))
    if count > solutions_to_exceed:
        break
    print(sorted(sol_set))
    count = 0;
