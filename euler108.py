import math

# 1/x + 1/y = 1/n ==> xy /(y+x) = n ==> nx + ny = xy
# nx and ny will always have gcd n
# for any n, x = 2*n and y = 2*n is always a solution.  This is the solution where x is largest and y is smallest.
# for any n, x = n+1, y = n*x = n*(n+1) is always a solution.  This is the solution where x is smallest and y is largest.
# n*(n+1) + n*n*(n+1) = (n+n^2)*(n+1) = n*(n^2 + 1) * (n+1)

# gcd(x,y) = x or some prime factor of x, given x is the smaller one
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def extendedEuclid(a, b):
    """
    Preconditions - a and b are both positive integers.
    Posconditions - The equation for ax+by=gcd(a,b) has been returned where
                    x and y are solved.
    Input - a : int, b : int
    Output - ax+by=gcd(a,b) : string
    """
    b, a = max(a, b), min(a, b)
    # Format of euclidList is for back-substitution
    euclidList = [[b % a, 1, b, -1 * (b // a), a]]
    while b % a > 0:
        b, a = a, b % a
        euclidList.append([b % a, 1, b, -1 * (b // a), a])
    if len(euclidList) > 1:
        euclidList.pop()
        euclidList = euclidList[::-1]
        for i in range(1, len(euclidList)):
            euclidList[i][1] *= euclidList[i - 1][3]
            euclidList[i][3] *= euclidList[i - 1][3]
            euclidList[i][3] += euclidList[i - 1][1]

    expr = euclidList[len(euclidList) - 1]
    strExpr = str(expr[1]) + "*" + str(expr[2]) + " + " + str(expr[3]) + "*" + str(expr[4]) \
              + " = " + str(euclidList[0][0])
    return strExpr

#test = [24,78,360,15620,6400,1100,150000]
print("{}".format(extendedEuclid(840,840)))
gcd,x,y = egcd(840,840);
print("{} {} {}".format(gcd,x,y))
test = [24]
nstart = 2
nmax = 100
solutions_to_exceed = 1000
count = 0
#for n in range(nstart, nmax+1):
for n in test:
    print("\n({}): ".format(n), end="")
    y_max = n * (n + 1)
    for x in range(n+1, 2*n+1):
        if count > solutions_to_exceed:
            break
        for y in range(2*n, n*(n+1)+1):
            print("({},{}): {}, ".format(x,y, egcd(x,y)))
            print("{}".format(extendedEuclid(x,y)))
            if math.gcd(x,y) > 1:
                xy = x * y
                if xy % n == 0:
                    nx_plus_ny = n * x + n * y
                    if xy == nx_plus_ny:
                        count+=1
                        y_max = y
                        print("{},{}".format(x, y))
                        break
                    if xy > nx_plus_ny:
                        break
    print("\n({}): {}".format(n, count), end="")
    if count > solutions_to_exceed:
        break
    count = 0;
