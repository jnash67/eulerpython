import eulerutils as eu

def is_nine_digit_pandigital(numList):
    allstr = ""
    for a in numList:
        allstr = allstr + str(a)
    resultSet = set()
    found = True
    for char in allstr:
        if char in resultSet:
            found = False
        else:
            resultSet.add(char)
    if found:
        if len(resultSet)==9:
            if not('0' in resultSet):
                # we have one
                return int(allstr)
    return 0

# pandigital use all digits from 1-9
# num-digit pandigital makes use of all digits 1 to num
def is_n_digit_pandigital(num, n):
    allstr = str(num)
    resultSet = set()
    noduplicates = True
    for char in allstr:
        digChar = int(char)
        if digChar in resultSet:
            noduplicates = False
        else:
            resultSet.add(digChar)
    if noduplicates:
        if not(0 in resultSet):
            if not(eu.collectionutils.any_greater_than_n_in_number_list(resultSet, n)):
                # we have one
                return True
    return False

# here we have pandigitals that use 0-9
def is_ten_digit_pandigital(numstr):
    resultSet = set()
    noduplicates = True
    for char in numstr:
        digChar = int(char)
        if digChar in resultSet:
            noduplicates = False
        else:
            resultSet.add(digChar)
    if noduplicates:
        return True
    return False