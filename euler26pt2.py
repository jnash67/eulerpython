import scs
from collections import namedtuple

def run_SCS_algorithms(sequences):
        sequences = scs.remove_redundant_sequences(sequences, debug=True)
        lowerbound, upperbound = scs.lower_bound(sequences), scs.upper_bound(sequences)
        print ("Lowerbound on Shortest Common Supersequence:", lowerbound)
        print ("Upperbound on Shortest Common Supersequence:", upperbound)
        solutions = scs.backtrack_shortest_common_supersequences(sequences, upperbound)
        print ("Backtrack found %s SCSs of optimal length %s."%(len(solutions), len(solutions[0])))
        print ("E.g.", solutions[0], "is valid:", scs.is_supersequence_of_sequences(solutions[0], sequences))
        # x = namedtuple()
        # scs.pretty_print_scs_with_sequences((solutions[0], sequences))

sequences_1 = [ [1,2,3],
                [1,2,5],
                [3,1,5,4],
                [1,2,1,5],
                [1,2,5]]

sequences_2 = [ [1,2,1,2,3],    # "acacg"
                [1,4,1,3,1],    # "ataga"
                [2,1,2,3,4],    # "cacgt"
                [3,4,1,1,4]]    # "ctaat"

sequences_3 = [ [5,2,1,6,3,6,3,1],
                [1,4,1,3,1,5,1,2],
                [2,1,6,3,4,4,2,3],
                [3,4,5,1,4,6,1,2]]

sequences_4 = [ [5,1,3,5,2,6],
                [1,5,2,1,3,2,3,1],
                [5,1,3,5,2,1,6,2],
                [3,5,1,6,2,4,6,1,2]]

run_SCS_algorithms(sequences_4)