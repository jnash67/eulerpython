import eulerutils as eu
from fractions import Fraction

def farey(limit):
    '''Fast computation of Farey sequence as a generator'''
    # num, d is the start fraction num/d (0,1) initially
    # N, D is the stop fraction N/D (1,1) initially
    pend = []
    n = 0
    d = N = D = 1
    while True:
        mediant_d = d + D
        if mediant_d <= limit:
            mediant_n = n + N
            pend.append((mediant_n, mediant_d, N, D))
            N = mediant_n
            D = mediant_d
        else:
            yield n, d
            if pend:
                n, d, N, D = pend.pop()
            else:
                break

# num, d is the start fraction num/d
# N, D is the stop fraction N/D
def farey_range(limit,n=0,d=1,N=1,D=1):
    '''Fast computation of Farey sequence as a generator'''
    pend = []
    while True:
        mediant_d = d + D
        if mediant_d <= limit:
            mediant_n = n + N
            pend.append((mediant_n, mediant_d, N, D))
            N = mediant_n
            D = mediant_d
        else:
            yield n, d
            if pend:
                n, d, N, D = pend.pop()
            else:
                break



def relatively_prime_generator(n, a=1, b=1):
    ### generates all relatively prime pairs <= num. The larger number comes first.
    yield (a,b)
    k = 1
    while a*k+b <= n:
        for i in relatively_prime_generator(n, a*k+b, a):
            yield i
        k += 1

onethird = Fraction(1,3)
onehalf = Fraction(1,2)

count = 0
for f in farey_range(12000,1,3,1,2):
    num = f[0]
    den = f[1]
    f = Fraction(num,den)
    if onehalf > f > onethird:
        count+=1

print(count)

