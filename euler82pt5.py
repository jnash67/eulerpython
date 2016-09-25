import eulerutils as eu
import numpy as np
import sortedcontainers as sc
import time

def load():
    global nodes
    nodes = np.empty((size, size), dtype=object)
    lineCount = 0
    for line in list(open(file)):
        line = line.strip()
        listOfStr = line.split(",")
        listOfInt = list(map(int, listOfStr))
        numCount = -1
        for i in listOfInt:
            numCount += 1
            nodes[lineCount][numCount] = i
        lineCount += 1


# file = "matrix1.txt"
# size = 5
# file = "tinymatrix.txt"
# size = 2
file = "p082_matrix.txt"
size = 80

# num = np.zeros((size,size))
# nodes is zero-based array but rows & columns for table are 1-based
nodes = np.empty((size, size), dtype=object)
load()

start = time.time()

# for all the end points
graph = eu.graph.matrix_to_graph(nodes, size)
eu.graph.set_first_column_as_start_point(graph, nodes, size)

end_points = sc.SortedDict()
for end_row in range(1, size + 1):
    end_name = eu.graph.vertex_name(end_row, size)
    end_points[end_name] = (end_row - 1, size - 1)

minsum = float("inf")
minpath = ''
for end_name in end_points.keys():
    sp = eu.graph.run_dijkstra(graph, end_name)
    sum = 0
    for i in range(0, len(sp) - 1):
        edge_len = graph[sp[i]][sp[i + 1]]
        sum = sum + edge_len
    if (sum < minsum):
        minsum = sum
        minpath = sp
        minend_name = end_name
        print("NEW ABS MIN: ending at {} sum is {} for path {}".format(end_name, sum, sp))

print("Absolute min ending at {} sum is {} for path {}".format(minend_name, minsum, minpath))
finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))
