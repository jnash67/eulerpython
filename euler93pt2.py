import sympy
import itertools
import sortedcontainers as sc
import eulerutils as eu
import decimal


def calc_rpn(istr):
    try:
        rp = eu.rpn.rpn_calc(eu.rpn.get_input(istr))
        result = decimal.Decimal(rp[-1][2])
        if result > 0:
            if int(result) == result:
                return int(result)
        return 0
    except ZeroDivisionError as error:
        return 0

def last_consecutive(results):
    maxr = max(results)
    for i in range(1, maxr):
        if not i in results:
            return i-1
    return maxr


# for each combination of digits
# for each combination of operators with replacement
# for each addition of sets of parens. an open paren can go before each digit operator pair.  A close paren can
# go after each digit

alldigs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#alldigs = [1,2,3,4]
# alldigs = [4,5,7,8]
# alldigs = [2,6,7,9]
# alldigs = [2,3,8,9]
operators = ['+', '-', '*', '/']
results = sc.SortedSet()

# input = ['1','2','+']
#inputstr = '4 3 * 2 * 1 -'
#inputstr = '3 4 * 1 - 2 *'
# rp = eu.rpn.rpn_calc(eu.rpn.get_input(inputstr))
# print(rp[-1][2])

#result = eu.rpnconvert.rpn_to_infix(inputstr)
#print(result)

max_last_consecutive = 0
for d1 in itertools.combinations(alldigs,4):
    for d in itertools.permutations(d1, 4):
        for o1 in itertools.combinations_with_replacement(operators, 3):
            for o in itertools.permutations(o1, 3):
                dstr = " ".join(map(str, d))
                ostr = " ".join(map(str, o))
                istr = dstr + " " + ostr
                result = calc_rpn(istr)
                if result > 0:
                    results.add(result)
                istr = str(d[0]) + " " + str(d[1]) + " " + o[0] + " " + str(d[2]) + " " + o[
                    1] + " " + str(d[3]) + " " + o[2]
                result = calc_rpn(istr)
                if result > 0:
                    results.add(result)
                istr = str(d[0]) + " " + str(d[1]) + " " + str(d[2]) + " " + o[
                    0] + " " + o[1] + " " + str(d[3]) + " " + o[2]
                result = calc_rpn(istr)
                if result > 0:
                    results.add(result)
    r = last_consecutive(results)
    if r > max_last_consecutive:
        max_last_consecutive = r
        print("Highest consec is {}, max is {}, count is {}, for {} -> {}".format(r, max(results), len(results),  sorted(d1), results))

# print(results)
# print("Count is " + str(len(results)))

