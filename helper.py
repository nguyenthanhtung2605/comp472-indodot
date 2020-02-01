from solver import depth_first_search


def puzzles_reader(input_file):
    puzzle_list = list()
    with open(input_file, 'r') as file:
        for each in file:
            print(each)
            puzzle = dict()
            parts = (str(each).split(' ', 4))

            puzzle['size'] = int(parts[0])
            puzzle['max_d'] = int(parts[1])
            puzzle['max_l'] = int(parts[2])
            puzzle['board'] = parts[3]
            puzzle['is_solved'] = False
            puzzle_list.append(puzzle)

    return puzzle_list

# def dfs_call(input_file, out_file):
def dfs_call(input_file):  # to be removed
    puzzle_list = puzzles_reader(input_file)
    for puzzle in puzzle_list:
        visited = set()
        depth_first_search(puzzle, 0, visited)


def write_to_file():
    file_path = ''
    return file_path

if __name__ == '__main__':
    input_file = '/Users/i505690/PycharmProjects/comp472-indodot/data/puzzles_test'
    dfs_call(input_file)




