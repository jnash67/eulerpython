
def number_of_non_repeating_terms_in_factorial_chain(n):
    global digit_facts
    sumoffact = 0
    strn = str(n)
    terms = set()
    terms.add(n)
    while sumoffact != n:
        sumoffact = 0
        for strdig in strn:
            dig = int(strdig)
            sumoffact+=digit_facts[dig]
        if not sumoffact in terms:
            terms.add(sumoffact)
            strn = str(sumoffact)
        else:
            break
    return len(terms)


# 0! is 1, 1! is 1 ...
digit_facts = [1,1,2,6,24,120,720,5040,40320,362880]

# print("145 chain is {} ".format(number_of_non_repeating_terms_in_factorial_chain(145)))
# print("169 chain is {} ".format(number_of_non_repeating_terms_in_factorial_chain(169)))
# print("871 chain is {} ".format(number_of_non_repeating_terms_in_factorial_chain(871)))
# print("872 chain is {} ".format(number_of_non_repeating_terms_in_factorial_chain(872)))
# print("69 chain is {} ".format(number_of_non_repeating_terms_in_factorial_chain(69)))
# print("78 chain is {} ".format(number_of_non_repeating_terms_in_factorial_chain(78)))
# print("540 chain is {} ".format(number_of_non_repeating_terms_in_factorial_chain(540)))

size = 1000000
chainsof60 = 0
for i in range(1,size+1):
    chain = number_of_non_repeating_terms_in_factorial_chain(i)
    if (chain == 60):
        print("Chain starting with {} has 60 terms".format(i))
        chainsof60+=1

print("There are {} chains of 60".format(chainsof60))
