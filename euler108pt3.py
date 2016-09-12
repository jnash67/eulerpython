# 1/x + 1/y = 1/n ==> xy /(y+x) = n ==> nx + ny = xy
# This diophantine equation only has solutions if n divides xy with no remainder
# nx and ny will always have gcd n
# for any n, x = 2*n and y = 2*n is always a solution.  This is the solution where x is largest and y is smallest.
# for any n, x = n+1, y = n*x = n*(n+1) is always a solution.  This is the solution where x is smallest and y is largest.
# n*(n+1) + n*n*(n+1) = (n+n^2)*(n+1) = n*(n^2 + 1) * (n+1)

# This uses a binomial tree spanning algorithm

#test = [24,78,360,15620,6400,1100,150000]

test=[1260]
nstart = 2
nmax = 1000
solutions_to_exceed = 1000
count = 0
#for n in range(nstart, nmax + 1):
for n in test:
    #print("\n({}): ".format(n), end="")
    y_max = n * (n + 1) + 1
    for x in range(n + 1, 2 * n + 1):
        if count > solutions_to_exceed:
            break
        y_min = 2 * n - 1
        y = y_min + (y_max - y_min) // 2
        # prev_diff = abs(x * y - n * y + n * x)
        while True:
            xy = x * y
            nx_plus_ny = n * x + n * y
            # print("y: {}".format(y))
            # diff = abs(x * y - n * y + n * x)
            # print("diff: {}   prev diff: {}".format(diff, prev_diff))
            # prev_diff= diff
            if xy == nx_plus_ny:
                count += 1
                y_max = y
                #print("({},{}) ".format(x, y), end="", flush=True)
                break
            if xy > nx_plus_ny:
                y_max = y
                y = y_min + (y_max - y_min) // 2
            if xy < nx_plus_ny:
                y_min = y
                y = y_min + (y_max - y_min) // 2
            if y == y_min or y == y_max:
                break
    print("\n{}, {}".format(n, count), end="")
    if count > solutions_to_exceed:
        break
    count = 0;
