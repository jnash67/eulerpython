import itertools
import sortedcontainers as sc

# doesn't mean the first has to before the other first.
# in 123451, 3 does exist before a 1
def does_one_digit_exist_before_another_in_number(num, dig1, dig2):
    strnum = str(num)
    strdig1 = str(dig1)
    strdig2 = str(dig2)
    if strdig1 in strnum and strdig2 in strnum:
        firstindexof1 = strnum.index(strdig1)
        lastindexof2 = strnum.rindex(strdig2)
        return firstindexof1 < lastindexof2
    else:
        return False

file = "p079_keylog.txt"
text_file = open(file, "r")
strnums = text_file.readlines()
orig_unique_digits = sc.SortedSet()
strnums = [strnum.strip() for strnum in strnums]
for strnum in strnums:
    orig_unique_digits.add(strnum[0])
    orig_unique_digits.add(strnum[1])
    orig_unique_digits.add(strnum[2])
    print(strnum)
# for line in open(file):
#     print(line)

min_length = len(orig_unique_digits)
unique_digits = list(orig_unique_digits)
print("Unique digits --> {} with length {}".format(orig_unique_digits, min_length))
found = False
count = 0
while not found:
    for extra_l in range(0, min_length):
        if found:
            break
        for j in itertools.combinations(unique_digits, extra_l):
            if found:
                break
            unique_digits = orig_unique_digits
            for extra in j:
                unique_digits.append(extra)
            print("Starting on length {}".format(min_length+extra_l))
            for i in itertools.permutations(unique_digits, min_length+extra_l):
                count +=1
                if count % 1000000 == 0:
                    print("{}th million combination".format(count//1000000))
                found = True
                for strnum in strnums:
                    if not(does_one_digit_exist_before_another_in_number(i, strnum[0], strnum[1])):
                        found = False
                        break
                    if not(does_one_digit_exist_before_another_in_number(i, strnum[0], strnum[2])):
                        found = False
                        break
                    if not(does_one_digit_exist_before_another_in_number(i, strnum[1], strnum[2])):
                        found = False
                        break

                if found:
                    print("Number that fits is {} of length {}".format(i, min_length))
                    break



