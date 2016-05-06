from . import dijkstra
import sortedcontainers as sc


def vertex_name(row, col):
    return 'row:' + str(row) + ' ' + 'col:' + str(col)


def left_edge(row, col, nodes, size):
    if col == 1:
        # can't go left
        return None
    else:
        name = vertex_name(row, col - 1)
        dist = nodes[row - 1, col - 2]
        return name, dist


def right_edge(row, col, nodes, size):
    if col == size:
        # can't go right
        return None
    else:
        name = vertex_name(row, col + 1)
        dist = nodes[row - 1, col]
        return name, dist


def up_edge(row, col, nodes, size):
    if row == 1:
        # can't go up
        return None
    else:
        name = vertex_name(row - 1, col)
        dist = nodes[row - 2, col - 1]
        return name, dist


def down_edge(row, col, nodes, size):
    if row == size:
        # can't go down
        return None
    else:
        name = vertex_name(row + 1, col)
        dist = nodes[row, col - 1]
        return name, dist


def get_edges_up_down_right(row, col, nodes, size):
    edge_dict = {}
    right = right_edge(row, col, nodes, size)
    up = up_edge(row, col, nodes, size)
    down = down_edge(row, col, nodes, size)
    if not right is None:
        edge_dict[right[0]] = right[1]
    if not down is None:
        edge_dict[down[0]] = down[1]
    if not up is None:
        edge_dict[up[0]] = up[1]
    return edge_dict


def get_edges_up_down_left_right(row, col, nodes, size):
    edge_dict = get_edges_up_down_right(row,col, nodes, size)
    left = left_edge(row, col, nodes, size)
    if not left is None:
        edge_dict[left[0]] = left[1]
    return edge_dict


def matrix_to_graph_up_down_right(nodes, size):
    vertex_dict = sc.SortedDict()

    for row in range(1, size + 1):
        for col in range(1, size + 1):
            name = vertex_name(row, col)
            edge_dict = get_edges_up_down_right(row, col, nodes, size)
            vertex_dict[name] = edge_dict

    return vertex_dict


def matrix_to_graph_up_down_left_right(nodes, size):
    vertex_dict = sc.SortedDict()

    for row in range(1, size + 1):
        for col in range(1, size + 1):
            name = vertex_name(row, col)
            edge_dict = get_edges_up_down_left_right(row, col, nodes, size)
            vertex_dict[name] = edge_dict

    return vertex_dict


def set_top_left_as_start_point(graph, nodes, size):
    start_point = sc.SortedDict()
    start_name = vertex_name(1, 1)
    start_point[start_name] = nodes[0][0]
    graph['start'] = start_point


def set_first_column_as_start_point(graph, nodes, size):
    start_points = sc.SortedDict()
    for start_row in range(1, size + 1):
        start_name = vertex_name(start_row, 1)
        start_points[start_name] = nodes[start_row - 1][0]
    graph['start'] = start_points


def run_dijkstra(graph, end_name):
    # we should have turned the matrix into a graph
    # pointed the 'start' vertex to the points that can first be gotten to
    return dijkstra.shortestPath(graph, 'start', end_name)
