from math import sqrt


def puzzles_reader(input_file):
    puzzle_list = list()
    puzzleId = 1
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
    solution_file = open(prefix + "_solution.txt", 'w')
    search_file = open(prefix + "_search.txt", 'w')

    if len(path) == 0:
        solution_file.write('no solution')
    else:
        for step in path:
            solution_file.write(step + '\n')

    solution_file.close()

    for step in visited:
        search_file.write(step + '\n')

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


def flip_dot(index, puzzle, board):
    current_board = flip_single(index, board)

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


def get_num_of_zero_weighted(board, size):
    return 0


def get_num_of_zero(board):
    num = 0

    for ch in board:

        if ch == '0':
            num += 1

    return num


def get_connected_islands_count(board, puzzle_size):
    num = 0
    board_arr = [int(dot) for dot in board]

    for x in board_arr:
        if x == 1:
            num += 1
            sink(board_arr, x, puzzle_size)

    return num


def sink(board_arr, index, puzzle_size):
    if board_arr[index] == '1':
        board_arr[index] = '0'

        for i in range(4):
            neighbour = get_neighbour_index(0, index, puzzle_size)

            if neighbour > -1:
                sink(board_arr, neighbour, puzzle_size)


def format_index(index, board_size):
    if index is None:
        return "00"
    return chr(int(index / board_size) + 65) + str(int(index) % int(board_size))


# 0,1,2,3 => top, right, bottom, left
def get_neighbour_index(direction, index, puzzle_size):
    column_position = index % puzzle_size
    val = -1

    if direction == 0:
        if index - puzzle_size >= 0:
            val = index - puzzle_size

    elif direction == 1:
        if column_position < puzzle_size - 1:
            val = index + 1

    elif direction == 2:
        val = index + puzzle_size
        if val > puzzle_size * puzzle_size - 1:
            return -1

    elif direction == 3:
        if column_position > 0:
            val = index + 1

    if val > 0:
        return val

    return -1


def compute_h_simple(board, puzzle_size):
    return -get_num_of_zero(board)*2 + get_connected_islands_count(board, puzzle_size)


def write_to_file_node(prefix, size, node, search_path):
    solution_file = open(prefix + "_solution.txt", 'w')
    search_file = open(prefix + "_search.txt", 'w')

    print("path length: ", len(search_path))

    current_node = node

    arr = []
    while True:
        if current_node is None:
            break

        arr.insert(0, current_node)
        current_node = current_node.previous_node

    if len(arr) == 0:
        solution_file.write('no solution')
        print('>> No Solution\n')
    else:
        print('>> Solved\n')
        for s in arr:
            solution_file.write(format_index(s.previous_index, size) + "  " + s.board_state + '\n')

    for step in search_path:
        search_file.write(str(step.f) + "  " + str(step.g) + "  " + str(step.h) + "  " + step.board_state + '\n')

    solution_file.close()
    search_file.close()


class Node:
    board_state = None
    previous_node = None
    previous_index = 0
    previous_index_formated = None
    h = 0
    g = 0
    f = 0

    def __init__(self, h, board_state, previous_node, previous_index, is_astar=False):
        self.board_state = board_state
        self.previous_node = previous_node
        self.previous_index = previous_index
        self.previous_index_formated = format_index(previous_index, sqrt(len(board_state)))
        self.h = h
        if is_astar and previous_node is not None:
            self.g = previous_node.g + 1
            self.f = h + self.g
        else:
            self.f = h

    def __lt__(self, other):
        if self.f == other.f:
            return get_firstzero_index(self.board_state) < get_firstzero_index(other.board_state)

        return self.f < other.f
