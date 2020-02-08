from copy import deepcopy
from collections import deque
import helper


def search(puzzle):
    print('Solving puzzle #', puzzle['id'])
    visited = dict()
    solution_path = deque()
    search_path = deque()
    visited[str(puzzle['board'])] = 1

    depth_first_search(puzzle, 1, visited, puzzle['board'], solution_path, search_path)

    if len(solution_path) > 0:
        solution_path.insert(0, "0   " + str(puzzle['board']))
    search_path.insert(0, "0   " + str(puzzle['board']))

    helper.write_to_file(str(puzzle['id']) + "_dfs", search_path, solution_path)
    print('>> Solved\n')


def depth_first_search(puzzle, depth, visited, parent, solution_path, search_path):
    if depth == puzzle['max_d']:
        return False

    index = 0
    skip = False

    while index < len(str(puzzle['board'])) and not skip:

        temp_board = helper.flip_dot(index, puzzle)

        if (temp_board not in visited or (temp_board in visited and visited.get(temp_board) > depth)) and parent != temp_board:

            board_state = helper.format_index(index, puzzle['size']) + "  " + temp_board
            # print(board_state)

            # winning condition
            if helper.is_win(temp_board):
                solution_path.append(board_state)
                search_path.append(board_state)
                skip = True
            else:
                visited[temp_board] = depth
                search_path.append(board_state)

                temp_puzzle = deepcopy(puzzle)
                temp_puzzle['board'] = temp_board

                if depth_first_search(temp_puzzle, depth + 1, visited, temp_board, solution_path, search_path):
                    solution_path.insert(0, board_state)
                    skip = True
                else:
                    skip = False

        index += 1

    return skip
