"""
Leslie Horace
TSP: Uses the Nearest Neighbor Heuristic to greedily compute the Traveling Salesman Problem
Input: Adjacency matrix of weighted edges for a complete or incomplete graph
    G = [[0, 2, 3, 20, 1], [2, 0, 15, 2, 20], [3, 15, 0, 20, 13], [20, 2, 20, 0, 9], [1, 20, 13, 9, 0]]
    *Incomplete graphs use weight of 0 for non existent edge*
    *source is always G[0][0]=0
Output: List of traveled nodes to represent TSP tour
    Result = [0, 4, 3, 1, 2, 0]
"""


def solve_tsp(G):
    src = G[0][0]
    node = src
    visited = []
    while node not in visited:  # loop until all nodes are visited
        curr_edges = G[node]  # set current edges for current node
        visited.append(node)  # add node to visited
        min_node = node  # set min node to current node
        min_edge = curr_edges[node]  # set min edge to current nodes weight
        for v in range(len(curr_edges)):  # loop through all the next vertexes
            if v not in visited:  # check if the current vertex has not been visited
                # check if the min node is still current node OR if not, check if it has a valid smaller weight
                if min_node == node or min_node != node and 0 < curr_edges[v] < min_edge:
                    min_node = v  # set the min node to current vertex
                    min_edge = curr_edges[v]  # set the min edge to the current vertexes weight
        if min_node != node:  # check if the min node is not the current node
            node = min_node  # set current node to the minimum node
    visited.append(src)  # add source node to visited for the way back
    return visited  # return visited nodes list
