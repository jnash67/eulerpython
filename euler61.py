import time

import eulerutils as eu
import itertools
import sortedcontainers as sc


def delete_all_numbers_with_first_digits_not_as_last_digits_in_at_least_two_sets(listOfAll):
    global removed

    for l in listOfAll:
        for n in l:
            firstTwoDigits = eu.number.first_n_digits(n, 2)
            cnt = how_many_sets_have_numbers_with_first_two_digits(firstTwoDigits, listOfAll)
            # subtract 1 since the set we know the number is part of is in the list of sets
            if not (cnt - 1 >= 2):
                del (l[l.index(n)])
                removed += 1


def delete_all_numbers_with_last_digits_not_as_first_digits_in_at_least_two_sets(listOfAll):
    global removed

    for l in listOfAll:
        for n in l:
            lastTwoDigits = eu.number.last_n_digits(n, 2)
            cnt = how_many_sets_have_numbers_with_first_two_digits(lastTwoDigits, listOfAll)
            # subtract 1 since the set we know the number is part of is in the list of sets
            if not (cnt - 1 >= 2):
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
        if eu.number.last_n_digits(triangle, 2) > 10:
            triangulars.append(triangle)
        else:
            removed += 1
    if eu.number.num_digits(square) == 4:
        if eu.number.last_n_digits(square, 2) > 10:
            squares.append(square)
        else:
            removed += 1
    if eu.number.num_digits(pentagonal) == 4:
        if eu.number.last_n_digits(pentagonal, 2) > 10:
            pentagonals.append(pentagonal)
        else:
            removed += 1
    if eu.number.num_digits(hexagonal) == 4:
        if eu.number.last_n_digits(hexagonal, 2) > 10:
            hexagonals.append(hexagonal)
        else:
            removed += 1
    if eu.number.num_digits(heptagonal) == 4:
        if eu.number.last_n_digits(heptagonal, 2) > 10:
            heptagonals.append(heptagonal)
        else:
            removed += 1
    if eu.number.num_digits(octagonal) == 4:
        if eu.number.last_n_digits(octagonal, 2) > 10:
            octagonals.append(octagonal)
        else:
            removed += 1
    if (triangle > maxn) and (square > maxn) and (pentagonal > maxn) and (hexagonal > maxn) and (
                heptagonal > maxn) and (octagonal > maxn):
        break

print(
    "There are {} triangulars, {} squares, {} pentagonals, {} hexagonals, {} heptagonals, {} octagonals with second to last digit not zero".
        format(len(triangulars), len(squares), len(pentagonals), len(hexagonals), len(heptagonals), len(octagonals)))
print("{} were removed".format(removed))

removed = 0
listOfAll = triangulars, squares, pentagonals, hexagonals, heptagonals, octagonals
# The last two digits of each number in a set must be the first two digits in at least two other sets to be
# worth keeping
delete_all_numbers_with_last_digits_not_as_first_digits_in_at_least_two_sets(listOfAll)

print(
    "There are {} triangulars, {} squares, {} pentagonals, {} hexagonals, {} heptagonals, {} octagonals with last two digits not the first two digits in at least two other sets".
        format(len(triangulars), len(squares), len(pentagonals), len(hexagonals), len(heptagonals), len(octagonals)))
print("an additional {} were removed".format(removed))

# likewise, the first two digits of each number in a set must be the last two digits in at least two other sets to be
# worth keeping
removed = 0
delete_all_numbers_with_first_digits_not_as_last_digits_in_at_least_two_sets(listOfAll)
print(
    "There are {} triangulars, {} squares, {} pentagonals, {} hexagonals, {} heptagonals, {} octagonals with last two digits not the first two digits in at least two other sets".
        format(len(triangulars), len(squares), len(pentagonals), len(hexagonals), len(heptagonals), len(octagonals)))
print("an additional {} were removed".format(removed))
count = 0
start_time = time.time()
setOfEach = set()
setOfCycles = set()

# solve the problem for set of 3
# for tr in triangulars:
#     for sq in squares:
#         for pe in pentagonals:
#             tuple = tr,sq,pe
#             for i in itertools.permutations(tuple, 3):
#                 count += 1
#                 if (count % 1000000 == 0):
#                     print("{:,} combinations checked in {}".format(count, time.time()-start_time))
#                     start_time = time.time()
#                 if eu.number.last_n_digits(i[0], 2) == eu.number.first_n_digits(i[1], 2):
#                     if eu.number.last_n_digits(i[1], 2) == eu.number.first_n_digits(i[2], 2):
#                         if eu.number.last_n_digits(i[2], 2) == eu.number.first_n_digits(i[0], 2):
#                             print("RESULT: {}".format(i))
#                             break


count = 0
start_time = time.time()
permList = sc.SortedList()
for tr in triangulars:
    firsttwotr = eu.number.first_n_digits(tr, 2)
    lasttwotr =  eu.number.last_n_digits(tr, 2)
    for sq in squares:
        firsttwosq = eu.number.first_n_digits(sq, 2)
        lasttwosq =  eu.number.last_n_digits(sq, 2)
        for pe in pentagonals:
            firsttwope = eu.number.first_n_digits(pe, 2)
            lasttwope =  eu.number.last_n_digits(pe, 2)
            for hx in hexagonals:
                firsttwohx = eu.number.first_n_digits(hx, 2)
                lasttwohx =  eu.number.last_n_digits(hx, 2)
                for hp in heptagonals:
                    firsttwohp = eu.number.first_n_digits(hp, 2)
                    lasttwohp =  eu.number.last_n_digits(hp, 2)
                    for oc in octagonals:
                        tuple = sq,pe,hx,hp,oc
                        c = how_many_numbers_have_last_two_digits(firsttwotr, tuple)
                        if (c <2):
                            break
                        c = how_many_numbers_have_first_two_digits(lasttwotr, tuple)
                        if (c<2):
                            break
                        setOfEach.clear()
                        setOfEach.add(tr)
                        setOfEach.add(sq)
                        setOfEach.add(pe)
                        setOfEach.add(hx)
                        setOfEach.add(hp)
                        setOfEach.add(oc)
                        if len(setOfEach) == 6:
                            # if each number's first two digits aren't at least two other numbers last two digit's
                            # then skip this permutation
                            # skip = False
                            # for n in setOfEach:
                            #     firsttwo = eu.number.first_n_digits(n, 2)
                            #     c = how_many_numbers_have_last_two_digits(firsttwo, setOfEach)
                            #     # we add 1 because the n is part of the setOfEach
                            #     if c < 3:
                            #         skip = True
                            #         break
                            #     lasttwo =
                            #     c = how_many_numbers_have_first_two_digits(lasttwo, setOfEach)
                            #     if c < 3:
                            #         skip = True
                            #         break
                            # if not skip:
                                permList = sc.SortedList(itertools.permutations(setOfEach, 6))
                                permListWithoutCycles = []
                                while len(permList) > 0:
                                    i = permList[0]
                                    permListWithoutCycles.append(i)
                                    del (permList[0])
                                    del (permList[permList.index((i[5], i[0], i[1], i[2], i[3], i[4]))])
                                    del (permList[permList.index((i[4], i[5], i[0], i[1], i[2], i[3]))])
                                    del (permList[permList.index((i[3], i[4], i[5], i[0], i[1], i[2]))])
                                    del (permList[permList.index((i[2], i[3], i[4], i[5], i[0], i[1]))])
                                    del (permList[permList.index((i[1], i[2], i[3], i[4], i[5], i[0]))])
                                # cycles = set(i for i in itertrotations(setOfEach))
                                # tuple = tr,sq,pe,hx,hp,oc
                                # there are 720 permutations, however, we can exclude all cycles
                                # for i in itertools.permutations(setOfEach,6):
                                for i in permListWithoutCycles:
                                    count += 1
                                    if count % 1000000 == 0:
                                        print("{:,} combinations checked in {}".format(count, time.time() - start_time))
                                        start_time = time.time()
                                    if eu.number.last_n_digits(i[0], 2) == eu.number.first_n_digits(i[1], 2):
                                        if eu.number.last_n_digits(i[1], 2) == eu.number.first_n_digits(i[2], 2):
                                            if eu.number.last_n_digits(i[2], 2) == eu.number.first_n_digits(i[3], 2):
                                                if eu.number.last_n_digits(i[3], 2) == eu.number.first_n_digits(i[4],
                                                                                                                2):
                                                    if eu.number.last_n_digits(i[4], 2) == eu.number.first_n_digits(
                                                            i[5],
                                                            2):
                                                        if eu.number.last_n_digits(i[5], 2) == eu.number.first_n_digits(
                                                                i[0], 2):
                                                            print("RESULT: {}".format(i))
                                                            break
