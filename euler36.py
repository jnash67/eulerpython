
def dec_to_bin(x):
    return int(bin(x)[2:])

def is_palindrome(s):
    return str(s) == str(s)[::-1]


b = dec_to_bin(585)
print(b)

lim = 1000000
sumall = 0
for i in range(1, lim):
    if is_palindrome(str(i)):
        b = dec_to_bin(i)
        if is_palindrome(str(b)):
            # palindromic in both bases
            print("{} and {} are palindromic".format(i,b))
            sumall += i

print("Sum of all is {}".format(sumall))