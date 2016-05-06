import itertools


def magic3gon():
    global solutionsDict
    global solutionsList
    global maxsol
    for i in itertools.permutations(range(1, 7), 6):
        # the external nodes are the first nodes of each line
        line1node1 = i[0]
        line2node1 = i[3]
        line3node1 = i[5]
        line1node2 = i[1]
        line1node3 = i[2]
        line2node2 = line1node3
        line2node3 = i[4]
        line3node2 = line2node3
        line3node3 = line1node2
        line1sum = line1node1 + line1node2 + line1node3
        line2sum = line2node1 + line2node2 + line2node3
        line3sum = line3node1 + line3node2 + line3node3
        if line3sum == line2sum == line1sum:
            # find the minimum external node. we know none of them are equal.
            if (line1node1 < line2node1) and (line1node1 < line3node1):
                solutionTuple = line1node1, line1node2, line1node3, line2node1, line2node2, line2node3, line3node1, line3node2, line3node3
            elif (line2node1 < line1node1) and (line2node1 < line3node1):
                solutionTuple = line2node1, line2node2, line2node3, line3node1, line3node2, line3node3, line1node1, line1node2, line1node3
            else:
                solutionTuple = line3node1, line3node2, line3node3, line1node1, line1node2, line1node3, line2node1, line2node2, line2node3

            solint = int(''.join(map(str, solutionTuple)))
            if not solint in solutionsList:
                if solint > maxsol:
                    maxsol = solint
                solutionsList.append(solint)
                solutionsDict.setdefault(line1sum, []).append(int(solint))


def magic5gon(strlen):
    global solutionsDict
    global solutionsList
    global maxsol
    for i in itertools.permutations(range(1, 11), 10):
        # the external nodes are the first nodes of each line
        line1node1 = i[0]
        line2node1 = i[3]
        line3node1 = i[5]
        line4node1 = i[7]
        line5node1 = i[9]

        line1node2 = i[1]
        line1node3 = i[2]
        line2node2 = line1node3
        line2node3 = i[4]

        line3node2 = line2node3
        line3node3 = i[6]

        line4node2 = line3node3
        line4node3 = i[8]

        line5node2 = line4node3
        line5node3 = line1node2

        line1sum = line1node1 + line1node2 + line1node3
        line2sum = line2node1 + line2node2 + line2node3
        line3sum = line3node1 + line3node2 + line3node3
        line4sum = line4node1 + line4node2 + line4node3
        line5sum = line5node1 + line5node2 + line5node3

        if line5sum == line4sum == line3sum == line2sum == line1sum:
            # find the minimum external node. we know none of them are equal.
            if (line1node1 < line2node1) and (line1node1 < line3node1) and (line1node1 < line4node1) and (
                        line1node1 < line5node1):
                solutionTuple = line1node1, line1node2, line1node3, line2node1, line2node2, line2node3, line3node1, line3node2, line3node3, line4node1, line4node2, line4node3, line5node1, line5node2, line5node3
            elif (line2node1 < line1node1) and (line2node1 < line3node1) and (line2node1 < line4node1) and (
                        line2node1 < line5node1):
                solutionTuple = line2node1, line2node2, line2node3, line3node1, line3node2, line3node3, line4node1, line4node2, line4node3, line5node1, line5node2, line5node3, line1node1, line1node2, line1node3
            elif (line3node1 < line1node1) and (line3node1 < line2node1) and (line3node1 < line4node1) and (
                        line3node1 < line5node1):
                solutionTuple = line3node1, line3node2, line3node3, line4node1, line4node2, line4node3, line5node1, line5node2, line5node3, line1node1, line1node2, line1node3, line2node1, line2node2, line2node3
            elif (line4node1 < line1node1) and (line4node1 < line2node1) and (line4node1 < line3node1) and (
                        line4node1 < line5node1):
                solutionTuple = line4node1, line4node2, line4node3, line5node1, line5node2, line5node3, line1node1, line1node2, line1node3, line2node1, line2node2, line2node3, line3node1, line3node2, line3node3
            elif (line5node1 < line1node1) and (line5node1 < line2node1) and (line5node1 < line3node1) and (
                        line5node1 < line4node1):
                solutionTuple = line5node1, line5node2, line5node3, line1node1, line1node2, line1node3, line2node1, line2node2, line2node3, line3node1, line3node2, line3node3, line4node1, line4node2, line4node3
            else:
                print("WE SHOULD NEVER END UP HERE")

            solstr = ''.join(map(str,solutionTuple))
            solint = int(solstr)
            if (len(solstr)==strlen):
                if not solint in solutionsList:
                    if solint > maxsol:
                        maxsol = solint
                    solutionsList.append(solint)
                    solutionsDict.setdefault(line1sum, []).append(int(solint))
                    print(solstr)


solutionsDict = {}
solutionsList = []
maxsol = 0
#magic3gon()
magic5gon(16)
for k in sorted(solutionsDict.keys()):
    solutionList = solutionsDict[k]
    for s in solutionList:
        print("{}\t{}".format(k, s))
print("The max solution is {}".format(maxsol))
