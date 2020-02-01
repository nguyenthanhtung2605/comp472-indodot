"""
Player library containing basic move operations.
"""

import sys, getopt


def main(argv):
    input_file = ''
    search_algorithm = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -s <search-algorithm> -o <outputfile>')
        print(
            '>>> Search algorithms available: \n\t> dfs as for Depth-first search\n\t> bfs as for Best-first search\n\t> as for A* search')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -s <search-algorithm> -o <outputfile>')
            print(
                '>>> Search algorithms available: \n\t> dfs as for Depth-first search\n\t> bfs as for Best-first search\n\t> as for A* search')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg

        elif opt in ("-s", "--search"):
            input_file = arg

        elif opt in ("-o", "--ofile"):
            output_file = arg

    print('Input file is "', input_file)
    print('Search algorithm is "', search_algorithm)
    print('Output file is "', output_file)


if __name__ == "__main__":
    main(sys.argv[1:])

# def move_left(first_term, second_term):
#     return first_term + second_term
#
#
# def move_right(first_term, second_term):
#     return first_term - second_term
