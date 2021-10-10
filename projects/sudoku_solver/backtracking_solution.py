from sudoku import *


def solve(starting_board):
    """ solve the sudoku given an starting configuration of it """
    # create an instance of the sudoku from the sudoku class
    board = SudokuBoardBacktracking(starting_board)

    print("SUDOKU SOLVER", end="\n\n\n")
    print("NON SOLVED VERSION")
    board.print_board()

    backtracking_algorithm(board)

    print("SOLVED VERSION")
    board.print_board()

def backtracking_algorithm(board):
    """ the backtracking algorithm aplied to the sudoku solver """

    # 1 . Find some empty space
    index = board.empty_case()
    if index is None:
        return True
    else:
        # 2 . Attempt to place the digits 1-9 in that space and Check if that
        #     digit is valid in the current spot based on the current board
        for digit in range(1,10):
            try:
                board[index] = str(digit)
            except SudokuNotValid as e:
                board.backtrack()
            else:
                if backtracking_algorithm(board):
                    return True
        board.backtrack()
        return False

class SudokuBoardBacktracking(SudokuBoard):
    """
    a board class to facilitate the acces to the sudoku extended from SudokuBoard
    to accomodate the Backtracking solution

    parameters :
        board (list[list[str]]) : the board in the format of the list of lists of strings.
            (empty case == "." )

    Accessing :
        * you can access a case simply by using self[i,j]
        * you can modify a case simply by using self[i,j] = value
        i represent the index and j the columns
    """
    def __init__(self, board):
        super().__init__(board)
        self.changes = [] # a slack containing the assignements made


    def __setitem__(self, index, value):
        """
        special function to simplify the modification of an element to the the sudoku : self[index] = value

        modified from the original one to check the if the sudoku is valid after each assignment
        and add each assignement to the slack self.changes
        """
        if value not in [str(i) for i in range(1, 10)] and value != ".":
            # if the value isn't a string containing a number from 1 to 9
            # or "." for an empty case
            raise ValueError("value must be a string containing a number for 1 to 9 or '.' for an empty case")

        if type(index) is tuple:
            if len(index) == 2:
                self.changes.append(index)
                row, column = index
                self.board[row][column] = str(value)
                # check if valid
                if not self.is_valid(value, row, column):
                    raise SudokuNotValid("This sudoku isn't valid")
            else:
                raise IndexError("the index is a tuple (i,j)")
        else:
            raise TypeError("The index Type is a tuple (i,j)")
        # raise exeptions in the else's

    def backtrack(self):
        """ pop the slack self.changes and update the board """
        try:
            index_to_change = self.changes.pop()
        except IndexError as e:
            return
        else:
            self.board[index_to_change[0]][index_to_change[1]] = "."

    def is_valid(self, value, row_index, column_index):
        """ check if the sudoku is still correct after adding a number to it """
        # 1. check that the line don't contain the same number twice
        for column in range(len(self.board)):
            if self.board[row_index][column] == value and column != column_index:
                return False

        # 2. check that the column don't contain the same number twice
        for row in range(len(self.board)):
            if self.board[row][column_index] == value and row != row_index:
                return False

        # 3. check the 3*3 matrice
        box_y = row_index // 3
        box_x = column_index // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == value and (i,j) != (row_index, column_index):
                    return False
        return True
