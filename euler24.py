import itertools

# itertools returns in lexicographic order
count = 0
for c in itertools.permutations("0123456789"):
    count += 1
    if (count % 1000 == 0):
        print("Count is " + str(count))
    if (count == 1000000):
        print(c)
        break