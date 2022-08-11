"""
Leslie Horace
Puzzle.py: Uses Depth First Search to min the minimum path from source => destination
Input: Adjacency Matrix, source node, destination node
        '#': represents a blocked wall
        '-': represents a open move
        board = [["-", "-", "-", "-", "-"],
                 ["-", "-", "#", "-", "-"],
                 ["-", "-", "-", "-", "-"],
                 ["#", "-", "#", "#", "-"],
                 ["-", "#", "-", "-", "-"]]
        source = (0,2)
        destination = (2,2)
Output: result = ([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')
        result[0] = array of coordinates for one of the shortest paths
        result[1] = string of directions for the minimum path
"""


def valid_move(board, next, visited):
    if next[0] < 0 or next[1] < 0:  # check if out out bounds
        return False
    elif next[0] >= len(board) or next[1] >= len(board[0]):  # check if out out bounds
        return False
    elif board[next[0]][next[1]] == "#":  # check if blocked
        return False
    elif next in visited:  # check if visited already
        return False
    else:
        return True


def find_paths(board, source, destination, visited, path, route):
    if source == destination:   # if target reach, return new path
        temp = [path], [route]
        return temp
    result = []  # array to store paths
    routes = []  # array to store routes
    moves = [(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]
    # iterate through each direction for current cell
    for x, y, z in moves:
        curr = source[0] + x, source[1] + y  # set current cell to source cells chosen direction
        if valid_move(board, curr, visited):
            visited.append(curr)    # add curr to visited array
            # recurse to obtain each possible path
            new_path = find_paths(board, curr, destination, visited, path + [curr], route + z)
            # if new path is found
            if new_path:
                result += new_path[0]    # add new path to result
                routes += new_path[1]    # add new path to routes
            visited.remove(curr)    # backtrack, remove current cell from visited
    return result, routes   # return the result


def solve_puzzle(board, source, destination):
    path = []
    res = find_paths(board, source, destination, [], path + [source], "")
    if res[0]:  # if result is not empty, return the minimum path and and associated route
        min_path = min(res[0], key=len)
        min_route = min(res[1], key=len)
        return min_path, min_route
    else:   # otherwise return none
        return None
