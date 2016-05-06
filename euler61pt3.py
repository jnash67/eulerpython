import time

import eulerutils as eu
import itertools
import sortedcontainers as sc


def delete_all_numbers_with_first_digits_not_as_last_digits_in_at_least_one_other_set(listOfAll):
    global removed

    for l in listOfAll:
        for n in l:
            firstTwoDigits = eu.number.first_n_digits(n, 2)
            cnt = how_many_sets_have_numbers_with_first_two_digits(firstTwoDigits, listOfAll)
            # subtract 1 since the set we know the number is part of is in the list of sets
            if not (cnt - 1 >= 1):
                del (l[l.index(n)])
                removed += 1


def delete_all_numbers_with_last_digits_not_as_first_digits_in_at_least_one_other_set(listOfAll):
    global removed

    for l in listOfAll:
        for n in l:
            lastTwoDigits = eu.number.last_n_digits(n, 2)
            cnt = how_many_sets_have_numbers_with_first_two_digits(lastTwoDigits, listOfAll)
            # subtract 1 since the set we know the number is part of is in the list of sets
            if not (cnt - 1 >= 1):
                del (l[l.index(n)])
                removed += 1


def how_many_sets_have_numbers_with_first_two_digits(lastTwoDigits, listOfAll):
    count = 0
    for l in listOfAll:
        for n in l:
            firstTwoDigits = eu.number.first_n_digits(n, 2)
            if firstTwoDigits == lastTwoDigits:
                count += 1
                break
    return count


def how_many_sets_have_numbers_with_last_two_digits(firstTwoDigits, listOfAll):
    count = 0
    for l in listOfAll:
        for n in l:
            lastTwoDigits = eu.number.last_n_digits(n, 2)
            if lastTwoDigits == firstTwoDigits:
                count += 1
                break
    return count


def how_many_numbers_have_last_two_digits(digitsToCheck, numberCollection):
    count = 0
    for n in numberCollection:
        lastTwoDigits = eu.number.last_n_digits(n, 2)
        if lastTwoDigits == digitsToCheck:
            count += 1
    return count


def how_many_numbers_have_first_two_digits(digitsToCheck, numberCollection):
    count = 0
    for n in numberCollection:
        firstTwoDigits = eu.number.first_n_digits(n, 2)
        if firstTwoDigits == digitsToCheck:
            count += 1
    return count


def each_item_in_only_on_list(items, allLists):
    for item in items:
        if item_in_only_one_list(item, allLists) is None:
            return False
    return True


def item_in_only_one_list(item, allLists):
    count = 0
    singleListItIsIn = None
    for l in allLists:
        if item in l:
            singleListItIsIn = l
            count += 1
        if count > 1:
            return None
    if count == 1:
        return l
    else:
        # in no list
        return None


def item_in_one_list_and_not_in_others(item, singleListItShouldBeIn, allLists):
    if not item in singleListItShouldBeIn:
        return False
    for l in allLists:
        if not (singleListItShouldBeIn == l):
            if item in l:
                return False
    return True


triangulars = sc.SortedList()
squares = sc.SortedList()
pentagonals = sc.SortedList()
hexagonals = sc.SortedList()
heptagonals = sc.SortedList()
octagonals = sc.SortedList()

# NOTE: The second from last digit cannot be zero or else the first digit of the next
# cycle would be less than 4 digits.
maxn = 10000
i = 0
removed = 0
while True:
    i += 1
    triangle = eu.triangular_number(i)
    square = eu.square_number(i)
    pentagonal = eu.pentagonal_number(i)
    hexagonal = eu.hexagonal_number(i)
    heptagonal = eu.heptagonal_number(i)
    octagonal = eu.octagonal_number(i)
    if eu.number.num_digits(triangle) == 4:
        triangulars.append(triangle)
    if eu.number.num_digits(square) == 4:
        squares.append(square)
    if eu.number.num_digits(pentagonal) == 4:
        pentagonals.append(pentagonal)
    if eu.number.num_digits(hexagonal) == 4:
        hexagonals.append(hexagonal)
    if eu.number.num_digits(heptagonal) == 4:
        heptagonals.append(heptagonal)
    if eu.number.num_digits(octagonal) == 4:
        octagonals.append(octagonal)
    if (triangle > maxn) and (square > maxn) and (pentagonal > maxn) and (hexagonal > maxn) and (
                heptagonal > maxn) and (octagonal > maxn):
        break

listOfAll = []
listOfAll.append(triangulars)
listOfAll.append(squares)
listOfAll.append(pentagonals)
listOfAll.append(hexagonals)
listOfAll.append(heptagonals)
listOfAll.append(octagonals)

# iterate through all the orders of types of numbers.  For example, the 1st could be triangle, second
# square etc.
listsOrder = [0,1,2,3,4,5]
for i in itertools.permutations(listsOrder,6):
    for l1 in listOfAll[i[0]]:
        firsttwol1 = eu.number.first_n_digits(l1,2)
        lasttwol1 = eu.number.last_n_digits(l1, 2)
        for l2 in listOfAll[i[1]]:
            # only continue if we have an l2 that continues the cycle
            if (lasttwol1 == eu.number.first_n_digits(l2,2)):
                lasttwol2 = eu.number.last_n_digits(l2, 2)
                for l3 in listOfAll[i[2]]:
                    if (lasttwol2 == eu.number.first_n_digits(l3,2)):
                        lasttwol3 = eu.number.last_n_digits(l3, 2)
                        for l4 in listOfAll[i[3]]:
                            if (lasttwol3 == eu.number.first_n_digits(l4,2)):
                                lasttwol4 = eu.number.last_n_digits(l4, 2)
                                for l5 in listOfAll[i[4]]:
                                    if (lasttwol4 == eu.number.first_n_digits(l5,2)):
                                        lasttwol5 = eu.number.last_n_digits(l5, 2)
                                        for l6 in listOfAll[i[5]]:
                                            if (lasttwol5 == eu.number.first_n_digits(l6,2)):
                                                lasttwol6 = eu.number.last_n_digits(l6,2)
                                                if lasttwol6 == firsttwol1:
                                                    # found
                                                    tuple = l1,l2,l3,l4,l5,l6
                                                    print("RESULT: {}".format(tuple))
                                                    print("Sum is {}".format(sum(tuple)))
                                                    print("Ordering is: {} where 0 is triangular, 1 is square etc.".format(i))
                                                    break