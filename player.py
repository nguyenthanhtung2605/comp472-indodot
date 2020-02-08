"""
Player library containing basic move operations.
"""

import getopt
import helper
import sys
import dfs


def main(argv):
    input_file = ''
    search_algorithm = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "hi:s:")
    except getopt.GetoptError:
        print('test.py -i <inputfile> -s <search-algorithm>')
        print(
            '>>> Search algorithms available: \n\t> dfs as for Depth-first search\n\t> bfs as for Best-first '
            'search\n\t> as for A* search')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -s <search-algorithm>')
            print(
                '>>> Search algorithms available: \n\t> dfs as for Depth-first search\n\t> bfs as for Best-first '
                'search\n\t> as for A* search')
            sys.exit()
        elif opt in "-i":
            input_file = arg

        elif opt in ("-s", "--search"):
            search_algorithm = arg

    puzzle_list = helper.puzzles_reader(input_file)
    for puzzle in puzzle_list:
        dfs.search(puzzle)


if __name__ == "__main__":
    main(sys.argv[1:])
