from copy import deepcopy


def best_first_search(puzzle):
    list_of_strings = ''
    return list_of_strings


def depth_first_search(puzzle, depth, visited):
    output_string = 'win'

    if is_win(str(puzzle['board'])):
        print(output_string)  # to be removed
        puzzle['is_solved'] = True
        return output_string

    visited.add(str(puzzle['board']))
    if depth == puzzle['max_d']:
        return

    index = 0
    skip = False

    while index < len(str(puzzle['board'])) and not skip:

        temp_board = flip_dot(index, puzzle)

        if temp_board not in visited:
            visited.add(temp_board)
            temp_puzzle = deepcopy(puzzle)
            temp_puzzle['board'] = temp_board

            result = depth_first_search(temp_puzzle, depth + 1, visited)

            if result == 'win':
                skip = True
            else:
                print("current Depth: " + str(depth))

        index += 1

    if skip:
        return output_string

def a_star_search(puzzle):
    list_of_strings = ''
    return list_of_strings


def is_win(board_state):
    parts = [int(dot) for dot in board_state]
    if sum(parts) == 0:
        return True
    else:
        return False


def flip_single(index, board):
    parts = [int(dot) for dot in board]
    print("current Index: " + str(index))
    print(board)
    if index >= (len(parts)) or index < 0:
        return board
    else:
        parts[index] = 1 - parts[index]
        return ''.join([str(dot) for dot in parts])


def flip_dot(index, puzzle):
    current_board = flip_single(index - 1, puzzle['board'])
    current_board = flip_single(index, current_board)
    current_board = flip_single(index + 1, current_board)
    current_board = flip_single(index + int(puzzle['size']), current_board)
    current_board = flip_single(index - int(puzzle['size']), current_board)

    return current_board


def get_firstzero_index(board):
    if str(board).find('0') < 0:
        return len(str(board)) + 1
    else:
        return str(board).find('0')


if __name__ == '__main__':
    puzzle = dict()
