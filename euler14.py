def collatz(n):
   yield n
   while n != 1:
     n = n / 2 if n % 2 == 0 else 3 * n + 1
     yield n

def collatz_count(n):
    c =0
    for val in collatz(n):
        c += 1
    return c


max = 0
maxi = 0
for i in range(1000000,1,-1):
    c = collatz_count(i)
    if (c>max):
        maxi=i
        max = c
        print("for collatz #{} the count is {}".format(i,max))

print(str(max) + "   " + str(maxi))

# num = 13
# print(num)
# for val in next_in_collatz_sequence(num):
#     print(val)
#
# print("============================")
# for val in collatz(13):
#     print(val)
#
# print(collatz_count(13))
#
# nics = next_in_collatz_sequence(num)
# print(nics)
# while (nics!=1):
#     nics = next_in_collatz_sequence(nics)
#     print(nics)