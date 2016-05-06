

unique = set()
for a in range(2,101):
    for b in range(2,101):
        val = a**b
        unique.add(val)

#s = sorted(list(unique))
print("Distinct items is " + str(len(unique)))