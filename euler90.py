import itertools

digits = ['0','1','2','3','4','5','6','7','8','9']
squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']
sixnine = ['6','9']

first_digit_of_squares = [0,1,2,3,4,6,8]
second_digit_of_squares = [1,4,5,6,4]
cubes_set = set()
unique_cubes_set = set()

valid_count  = 0
for c1 in itertools.combinations(digits, 6):
    for c2 in itertools.combinations(digits, 6):
        if c1 != c2:
            found = True
            for sq in squares:
                # the first and second chars of a square are never 6 and 9 or 9 and 6 together
                ch1 = sq[0]
                ch2 = sq[1]
                if ch1 in sixnine:
                    if not((ch2 in c2 and ('6' in c1 or '9' in c1)) or (ch2 in c1 and ('6' in c2 or '9' in c2))):
                        found = False
                elif ch2 in sixnine:
                    if not((ch1 in c2 and ('6' in c1 or '9' in c1)) or (ch1 in c1 and ('6' in c2 or '9' in c2))):
                        found = False
                elif not(((ch1 in c1) and (ch2 in c2)) or ((ch1 in c2) and (ch2 in c1))):
                    found = False

            if found:
                # c1, c2 are a valid pair
                if not((c1,c2) in cubes_set or (c2,c1) in cubes_set):
                    cubes_set.add((c1,c2))
                    unique_cubes_set.add(c1)
                    unique_cubes_set.add(c2)
                    print("{} and {} are valid cubes".format(c1,c2))
                    valid_count += 1

print("There are {} valid distinct arrangements".format(valid_count))
print("There are {} distinct cube arrangements".format(len(unique_cubes_set)))
