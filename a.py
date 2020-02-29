import heapq
from collections import deque

import helper
from helper import Node


def search(puzzle):
    print('Solving puzzle #', puzzle['id'])

    visited = set()
    search_path = deque()

    open_list = [Node(helper.compute_h_simple(puzzle['board'], puzzle['size']), puzzle['board'], None, None, True)]
    open_list_hashed = set()
    open_list_hashed.add(open_list[0].board_state)

    heapq.heapify(open_list)

    max_length = puzzle['max_l']

    while len(open_list) > 0 and max_length >= 0:
        max_length -= 1
        next_to_visit = heapq.heappop(open_list)
        open_list_hashed.remove(next_to_visit.board_state)

        # add to visited
        visited.add(next_to_visit.board_state)
        search_path.append(next_to_visit)

        # check for win condition
        if helper.is_win(next_to_visit.board_state):
            puzzle['is_solved'] = True
            break

        # expand children nodes
        generate_children(next_to_visit, open_list, visited, open_list_hashed, puzzle)

    if not puzzle['is_solved']:
        next_to_visit = None

    helper.write_to_file_node(str(puzzle['id']) + "_astar", puzzle['size'], next_to_visit, search_path)


def generate_children(node, open_list, visited, open_list_hashed, puzzle):
    for i in range(puzzle['size'] * puzzle['size']):
        temp_board = helper.flip_dot(i, puzzle, node.board_state)
        if temp_board not in visited and temp_board not in open_list_hashed:
            heapq.heappush(open_list,
                           Node(helper.compute_h_simple(temp_board, puzzle['size']), temp_board, node, i, True))
            open_list_hashed.add(temp_board)
