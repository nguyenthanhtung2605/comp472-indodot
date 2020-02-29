"""
Player library containing basic move operations.
"""

import getopt
import helper
import sys
import dfs
import a
import bfs


def main(argv):
    input_file = ''
    search_algorithm = 'DFS'

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
                'search\n\t>  astar as for A* search')
            sys.exit()
        elif opt in "-i":
            input_file = arg

        elif opt in ("-s", "--search"):
            search_algorithm = arg

    puzzle_list = helper.puzzles_reader(input_file)

    algo = ''

    if search_algorithm is None:
        search_algorithm = 'Depth-First'
        algo = dfs
    elif search_algorithm == 'astar':
        search_algorithm = 'A*'
        algo = a
    elif search_algorithm == 'bfs':
        search_algorithm = 'Best-First'
        algo = bfs
    else:
        search_algorithm = 'dfs'
        algo = dfs
        print('Unknown search Algo, will use default')

    print('Search algorithm is', search_algorithm)

    for puzzle in puzzle_list:
        algo.search(puzzle)


if __name__ == "__main__":
    main(sys.argv[1:])
