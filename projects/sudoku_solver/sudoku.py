""" This module contains basic functions to represent and interact with the sudoku """

def create_empty_board():
    """ a function that create an empty board """
    return [["." for _ in range(9)] for _ in range(9)]

class SudokuNotValid(Exception):
    """ This is a custo exception triggerd if the sudoku isn't valid """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'SudokuNotValid : ' + self.message


class SudokuBoard:
    """
    a board class to facilitate the acces to the sudoku
    ( you can extend this class to acomodate your own solution)

    parameters :
        board (list[list[str]]) : the board in the format of the list of lists of strings.
            (empty case == "." )

    Accessing :
        * you can access a case simply by using self[i,j]
        * you can modify a case simply by using self[i,j] = value
        i represent the index and j the columns
    """
    def __init__(self, board):
        self.board = board
        self.changes = []

    def __getitem__(self, index):
        """ special function to simplify acces to an element to the the sudoku : self[index] """
        if type(index) is tuple:
            if len(index) == 2:
                row, column = index
                return self.board[row][column]
            else:
                raise IndexError("the index is a tuple (i,j)")
        else:
            raise TypeError("The index Type is a tuple (i,j)")

    def __setitem__(self, index, value):
        """ special function to simplify the modification of an element to the the sudoku : self[index] = value """
        if value not in [str(i) for i in range(1, 10)] and value != ".":
            # if the value isn't a string containing a number from 1 to 9
            # or "." for an empty case
            raise ValueError("value must be a string containing a number for 1 to 9 or '.' for an empty case")

        if type(index) is tuple:
            if len(index) == 2:
                row, column = index
                self.board[row][column] = str(value)
            else:
                raise IndexError("the index is a tuple (i,j)")
        else:
            raise TypeError("The index Type is a tuple (i,j)")

    def __len__(self):
        """ special function to simplify acces to the dimensions of the board len(self)"""
        return (len(self.board), len(self.board[0]))

    def empty_case(self):
        """ a method that return the next empty case in the board """
        for i, line in enumerate(self.board):
            for j, case in enumerate(line):
                if case == ".":
                    return i, j
        return None

    def print_board(self):
        """ a method to print the board in the console """
        print("- "*12)
        for index, line in enumerate(self.board):
            print("", end="")
            for column, case in enumerate(line):
                if case == ".":
                    print(".", end=" ")
                elif case in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    print(case, end=" ")
                else:
                    # format of board error
                    raise ValueError("there is a problem with the format of the sudoku")

                if column in [2, 5]:
                    print(" | ", end="")

            if index in [2, 5, 8]:
                print()
                print("- "*12)
            else:
                print()

    @staticmethod
    def repetition_exist(my_list):
        """ a static method that return true is repetition of an element exist in a given list """
        elements = []
        for element in my_list:
            if element != ".":
                if element in elements:
                    return True
                else:
                    elements.append(element)
        return False
