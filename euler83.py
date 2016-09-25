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
file = "p083_matrix.txt"
size = 80

# num = np.zeros((size,size))
# nodes is zero-based array but rows & columns for table are 1-based
nodes = np.empty((size, size), dtype=object)
load()

start = time.time()

# for all the end points
graph = eu.graph.matrix_to_graph_up_down_left_right(nodes, size)
eu.graph.set_top_left_as_start_point(graph, nodes, size)

end_name = eu.graph.vertex_name(size, size)

sp = eu.graph.run_dijkstra(graph, end_name)
sum = 0
for i in range(0, len(sp) - 1):
    edge_len = graph[sp[i]][sp[i + 1]]
    sum = sum + edge_len

print("ABS MIN: ending at {} sum is {} for path {}".format(end_name, sum, sp))

finish = time.time()
print("Running Time: %.3f seconds" % (finish - start,))
