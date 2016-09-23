
allsum = 0
count = 0
# one should not be part of the range
for i in range(2, 1000000):
    stri = str(i)
    sum = 0
    for char in stri:
        sum = sum + int(char)**5
    if (i == sum):
        print("the fifth power of str_digits equals {}".format(i))
        allsum = allsum + sum
        count+=1

print("Sum of all of them is {}".format(allsum))
print("There are {} such numbers".format(count))