import eulerutils as eu
import numpy as np


def chain(n):
    global properDivisorArray
    chainList = []
    next_value_in_chain = n
    while not next_value_in_chain in chainList:
        chainList.append(next_value_in_chain)
        if next_value_in_chain > million:
            break
        if not properDivisorArray[next_value_in_chain] is None:
            pds = properDivisorArray[next_value_in_chain]
        else:
            pds = list(eu.number.find_all_proper_divisors(next_value_in_chain))
            properDivisorArray[next_value_in_chain] = sorted(pds)
        next_value_in_chain = sum(pds)
    chainList.append(next_value_in_chain)
    return chainList


def no_element_exceeding(chain, n):
    for link in chain:
        if link > n:
            return False
    return True


def is_amicable(chainList):
    if chainList[0] == chainList[-1]:
        return True
    return False

def len_of_chain(chain):
    return len(chain)-1

def smallest_element(chain):
    return sorted(chain)[0]

million = 10 ** 6
properDivisorArray = np.empty((million+1), dtype=object)
print(chain(28))
print(eu.number.find_all_proper_divisors(80196))
print(sum(eu.number.find_all_proper_divisors(80196)))
chain12496 = chain(12496)
print(chain12496)
print(is_amicable(chain12496))



chainDict = {}
longestLength = 0
amicableChains = []
for i in range(1, million + 1):
    chainList = chain(i)
    if is_amicable(chainList):
        # it's amicable
        amicableChains.append(chainList)
        chainLen =len_of_chain(chainList)
        if chainLen > longestLength:
            longestLength = chainLen
            print("Found new longest length {}. Smallest element is {}.  Chain is {}".format(
                longestLength, smallest_element(chainList), chainList))
        if chainLen == longestLength:
            print("Found EQUAL longest of length {}. Smallest element is {}.  Chain is {}".format(
                longestLength, smallest_element(chainList), chainList))
