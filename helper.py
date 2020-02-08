from dfs import depth_first_search


def puzzles_reader(input_file):
    puzzle_list = list()
    puzzleId = 0
    with open(input_file, 'r') as file:
        for each in file:
            puzzle = dict()
            parts = (str(each).split(' ', 4))

            puzzle['size'] = int(parts[0])
            puzzle['max_d'] = int(parts[1])
            puzzle['max_l'] = int(parts[2])
            puzzle['board'] = parts[3].strip()
            puzzle['is_solved'] = False
            puzzle['id'] = puzzleId
            puzzleId += 1
            puzzle_list.append(puzzle)

    return puzzle_list


def write_to_file(prefix, visited, path):
    solution_file = open(prefix+"_solution.txt", 'w')
    search_file = open(prefix+"_search.txt", 'w')

    if len(path) == 0:
        solution_file.write('no solution')
    else:
        for step in path:
            solution_file.write(step+'\n')

    solution_file.close()

    for step in visited:
        search_file.write(step+'\n')

    search_file.close()

def is_win(board_state):
    parts = [int(dot) for dot in board_state]
    if sum(parts) == 0:
        return True
    else:
        return False


def flip_single(index, board):
    parts = [int(dot) for dot in board]
    if index >= (len(parts)) or index < 0:
        return board
    else:
        parts[index] = 1 - parts[index]
        return ''.join([str(dot) for dot in parts])


def flip_dot(index, puzzle):
    current_board = flip_single(index, puzzle['board'])

    leftp = index % puzzle['size']
    if not leftp == 0:
        current_board = flip_single(index - 1, current_board)

    rightp = index % puzzle['size']
    if not rightp == puzzle['size'] - 1:
        current_board = flip_single(index + 1, current_board)

    current_board = flip_single(index + int(puzzle['size']), current_board)
    current_board = flip_single(index - int(puzzle['size']), current_board)

    return current_board


def get_firstzero_index(board):
    if str(board).find('0') < 0:
        return len(str(board)) + 1
    else:
        return str(board).find('0')


def format_index(index, board_size):
    return chr(int(index/board_size)+65) + str(int(index) % int(board_size))