import argparse
import json
import random

from sudoku import create_empty_board
from backtracking_solution import solve, backtracking_algorithm

def read_initial_config_json():
    json_path = "initial_instances.json"
    with open(json_path, 'r') as file:
        initial_conig_data = json.load(file)
    return initial_conig_data

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--given_board_index", help="""an integer defining which board to choose""")
    parser.add_argument("-empty", "--empty", action='store_true', help="""if given, the solver will start from an empty board""")
    parser.add_argument("-random", "--random", action='store_true', help="""if given, the solver will choose a random board""")
    return parser.parse_args()


def select_board():
    """ a function that select a board based on the arguments given to the program and json configuration file """
    args = parse_arguments()
    if args.empty:
        # if we give the "empty" argument then the initial board is gonna be empty
        return create_empty_board()
    else:
        initial_conig_data = read_initial_config_json()

        if args.random:
            return random.choice(initial_conig_data["starting_boards"])

        if args.given_board_index is None:
            board_index = initial_conig_data["default_board"]
        else:
            try:
                board_index = int(args.given_board_index)
            except ValueError as e:
                print("you must enter an interger as the board index")
                print(e)

            if board_index >= len(initial_conig_data["starting_boards"]):
                raise IndexError("the index you selected isn't valid there aren't that many boards in initial_configuration.json")

        return initial_conig_data["starting_boards"][board_index]

def main():
    # select a board based on the given args and the json arguments
    starting_board = select_board()
    solve(starting_board)


if __name__ == '__main__':
    main()
