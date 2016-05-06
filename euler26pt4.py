
# http://programmers.stackexchange.com/questions/192070/what-is-a-efficient-way-to-find-repeating-decimal
def f(n, d):
    x = n * 9
    z = x
    k = 1
    count = 0
    while z % d:
        count +=1
        z = z * 10 + x
        k += 1
        # this check is to keep it from going infinitely
        # when the decimal terminates
        if (count > 10000):
            return 0
    return k

max = 0
maxi =0
for i in range(2,1000):
    result = f(1,i)
    if not(result == 0):
        if (result > max):
            max = result
            maxi = i
        print("{} has repeating {}".format(i,result))
print("final max {} has repeating {}".format(maxi,max))
