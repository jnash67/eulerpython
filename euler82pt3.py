import eulerutils as eu
import numpy as np
import sortedcontainers as sc
import time

class Graph(object):
    ''' Graph object for matrix of problem 81'''

    def __init__(self, npmatrix):
        self.alist = {}
        self.alist[-1] = [(0, npmatrix[0,0])]
        for col in range(npmatrix.shape[1]):
            for row in range(npmatrix.shape[0]):
                index = npmatrix.shape[1] * row + col
                if index not in self.alist:
                    self.alist[index] = []
                if col < npmatrix.shape[1] - 1:
                    self.alist[index].append((index + 1, npmatrix[row,col+1]))
                if row < npmatrix.shape[0] - 1:
                    self.alist[index].append((index + npmatrix.shape[1], npmatrix[row+1, col]))

    def dijkstra_sp(self, source = -1):
        '''Dijkstra's shortest path algorithm - assumes all weights are positive'''
        distances = {source:0}
        edges = self.alist[source]
        while edges and len(distances) < len(self.alist):
            current_edge = edges.pop()
            if current_edge[0] not in distances:
                distances[current_edge[0]] = current_edge[1]
                new_edges = [(e[0], e[1] + current_edge[1]) for e in self.alist[current_edge[0]]]
                edges.extend(new_edges)
                edges.sort(key=lambda x: x[1], reverse=True)
        return distances

# graph = {'s': {'u': 10, 'x': 5}, 'u': {'v': 1, 'x': 2}, 'v': {'y': 4}, 'x': {'u': 3, 'v': 9, 'y': 2},
#          'y': {'s': 7, 'v': 6}}
#
# print(eu.dijkstra.shortestPath(graph, 's', 'v'))


def right_edge(x, y):
    global size
    global nodes
    if y == size - 1:
        return None
    else:
        name = str(x) + str(y + 1)
        dist = nodes[x, y + 1]
        return name, dist


def up_edge(x, y):
    global size
    global nodes
    if x == 0:
        return None
    else:
        name = str(x - 1) + str(y)
        dist = nodes[x - 1, y]
        return name, dist


def down_edge(x, y):
    global size
    global nodes
    if x == size - 1:
        return None
    else:
        name = str(x + 1) + str(y)
        dist = nodes[x + 1, y]
        return name, dist


def get_edges(x, y):
    global size
    global nodes
    name = str(x) + str(y)

    edge_dict = {}
    right = right_edge(x, y)
    up = up_edge(x, y)
    down = down_edge(x, y)
    if not right is None:
        edge_dict[right[0]] = right[1]
    if not down is None:
        edge_dict[down[0]] = down[1]
    if not up is None:
        edge_dict[up[0]] = up[1]
    return edge_dict


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


file = "matrix1.txt"
size = 5
# file = "tinymatrix.txt"
# size = 2
# file = "p082_matrix.txt"
# size = 80

# n = np.zeros((size,size))
nodes = np.empty((size, size), dtype=object)
load()

# start = time.time()
# graph = Graph(nodes)
# spaths = graph.dijkstra_sp()
# finish = time.time()
# print("Shortest Path Distance: %d" % spaths[nodes.size - 1])
# print("Running Time: %.3f seconds" % (finish - start,))



#nodes = np.fliplr(nodes)
vertex_dict = sc.SortedDict()

for i in range(0, size):
    for j in range(0, size):
        vertex_name = str(i) + str(j)
        edge_dict = get_edges(i, j)
        vertex_dict[vertex_name] = edge_dict

start_points = sc.SortedDict()
for start_row in range(0,size):
    start_name= str(start_row)+'0'
    start_points[start_name] = nodes[start_row][0]
vertex_dict['start'] = start_points

end_points = sc.SortedDict()
for end_row in range(0, size):
    end_name = str(end_row)+str(size-1)
    end_points[end_name]= (end_row, size-1)

minsum = float("inf")
minstart_name = ''
minend_name = ''
minpath = ''

for end_name in end_points.keys():
    s = start_points[start_name]
    sp =eu.dijkstra.shortestPath(vertex_dict, 'start', end_name)
    sum = 0
    for i in range(0,len(sp)-1):
        edge_len = vertex_dict[sp[i]][sp[i+1]]
        sum = sum + edge_len
    if (sum < minsum):
        minsum = sum
        minpath = sp
        minstart_name= start_name
        minend_name = end_name
        print("NEW ABS MIN: ending at {} sum is {} for path {}".format(end_name,sum, sp))

print("Absolute min starting at {} ending at {} sum is {} for path {}".format(minstart_name, minend_name, minsum, minpath))


minsum = float("inf")
minstart_name = ''
minend_name = ''
minpath = ''
for end_name in end_points.keys():
    endrowminsum = float("inf")
    endrowminstartname = ''
    endrowpath = ''
    for start_name in start_points.keys():
        s = start_points[start_name]
        vertex_dict['start'] = {start_name: nodes[s[0]][s[1]]}
        sp =eu.dijkstra.shortestPath(vertex_dict, 'start', end_name)
        sum = 0
        for i in range(0,len(sp)-1):
            edge_len = vertex_dict[sp[i]][sp[i+1]]
            sum = sum + edge_len
        if (sum < endrowminsum):
            endrowminsum = sum
            endrowminstartname = start_name
            endrowpath = sp
        if (sum < minsum):
            minsum = sum
            minpath = sp
            minstart_name= start_name
            minend_name = end_name
            #print("NEW ABS MIN: Starting at {} ending at {} sum is {} for path {}".format(start_name, end_name,sum, sp))
    print("Minimum sum for ending at {} starting at {} is {} with path {}".format(end_name, endrowminstartname, endrowminsum, endrowpath))

print("Absolute min starting at {} ending at {} sum is {} for path {}".format(minstart_name, minend_name, minsum, minpath))