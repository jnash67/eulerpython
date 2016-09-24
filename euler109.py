import time

start_time = time.time()
singles_str = ["S" + str(i) for i in range(1, 21)]
doubles_str = ["D" + str(i) for i in range(1, 21)]
triples_str = ["T" + str(i) for i in range(1, 21)]
singles_str.append("S25")
doubles_str.append("D50")
any_str = singles_str + doubles_str + triples_str

singles_int = [i for i in range(1, 21)]
doubles_int = [2 * i for i in singles_int]
triples_int = [3 * i for i in singles_int]
singles_int.append(25)
doubles_int.append(50)
any_int = singles_int + doubles_int + triples_int

total_distinct_checkouts = 0
for checkout_score in range(2,100):
# for checkout_score in range(6, 7):
    already_found = []
    distinct_checkouts_for_score = 0
    for dart1_str in any_str:
        index = any_str.index(dart1_str)
        dart1_val = any_int[index]
        if dart1_str[0] == 'D' and dart1_val == checkout_score:
            # done
            distinct_checkouts_for_score += 1
            #print("{}".format(dart1_str))
        else:
            for dart2_str in any_str:
                index = any_str.index(dart2_str)
                dart2_val = any_int[index]
                if dart2_str[0] == 'D' and dart1_val + dart2_val == checkout_score:
                    # done
                    distinct_checkouts_for_score += 1
                    #print("{}\t{}".format(dart1_str, dart2_str))
                else:
                    for dart3_str in doubles_str:
                        index = any_str.index(dart3_str)
                        dart3_val = any_int[index]
                        if dart3_str[0] == 'D' and dart1_val + dart2_val + dart3_val == checkout_score:
                                if not [dart1_str, dart2_str, dart3_str] in already_found:
                                    already_found.append([dart1_str, dart2_str, dart3_str])
                                    already_found.append([dart2_str, dart1_str, dart3_str])
                                    distinct_checkouts_for_score += 1
                                    #print("{}\t{}\t{}".format(dart1_str, dart2_str, dart3_str))
    print("{} checkouts for score of {}".format(distinct_checkouts_for_score, checkout_score))
    total_distinct_checkouts += distinct_checkouts_for_score
print("{} checkouts for entire range".format(total_distinct_checkouts))

finish_time = time.time()
print("Running Time: %.3f seconds" % (finish_time - start_time))
