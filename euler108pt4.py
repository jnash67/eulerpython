import time

# 1/x + 1/y = 1/n ==> xy /(y+x) = n ==> nx + ny = xy
# This diophantine equation only has solutions if n divides xy with no remainder
# for any n, x = 2*n and y = 2*n is always a solution.  This is the solution where x is largest and y is smallest.
# for any n, x = n+1, y = n*x = n*(n+1) is always a solution.  This is the solution where x is smallest and y is largest.
# n*(n+1) + n*n*(n+1) = (n+n^2)*(n+1) = n*(n^2 + 1) * (n+1)

# This uses a divide and conquer algorithm
start = time.time()

nstart = 420
max_count_so_far =0
nmax = 1000000
solutions_to_exceed = 1000
count = 0
for n in range(nstart, nmax + 1,420):
    y_max = n * (n + 1) + 1
    for x in range(n + 1, 2 * n + 1):
        y_min = 2 * n - 1
        y = y_min + (y_max - y_min) // 2
        while True:
            xy = x * y
            nx_plus_ny = n * x + n * y
            if xy == nx_plus_ny:
                count += 1
                y_max = y
                break
            if xy > nx_plus_ny:
                y_max = y
                y = y_min + (y_max - y_min) // 2
            if xy < nx_plus_ny:
                y_min = y
                y = y_min + (y_max - y_min) // 2
            if y == y_min or y == y_max:
                break
    if count > max_count_so_far:
        max_count_so_far = count
        print("({}): Max count so far {}".format(n, max_count_so_far))
    if count > solutions_to_exceed:
        break
    count = 0;

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))