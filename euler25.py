import math

def digits(n):
    d = int(math.log10(n))+1
    print(d)
    return d

def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

ind = 0
n = 0.0
while (n<1000.0):
    ind += 1
    f = fibonacci(ind)
    n = len(str(f))
    print("Fib {} has {} digits and is {}".format(ind,n, f))

print(f)
