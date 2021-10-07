from src.exceptions import AlreadySelectedError

class Board:

    def __init__(self):

        self.turn = "O"

        self._board = {
            (1,1) : None,
            (1,2) : None,
            (1,3) : None,
            (2,1) : None,
            (2,2) : None,
            (2,3) : None,
            (3,1) : None,
            (3,2) : None,
            (3,3) : None,
        }

        self._win_combinaisons = [
            ((1,1), (1,2), (1,3)),
            ((2,1), (2,2), (2,3)),
            ((3,1), (3,2), (3,3)),
            ((1,1), (2,1), (3,1)),
            ((1,2), (2,2), (3,2)),
            ((1,3), (2,3), (3,3)),
            ((1,1), (2,2), (3,3)),
            ((1,3), (2,2), (3,1)),
        ]

    def __getitem__(self, index):
        if index[0] > 3 or index[1] > 3 or index[0] < 1 or index[1] < 1:
            raise IndexError("")

        return self._board[index]

    def __setitem__(self, index, value):
        if index[0] > 3 or index[1] > 3 or index[0] < 1 or index[1] < 1:
            raise IndexError("")

        if value != "O" and value != "X":
            raise ValueError("")

        if self._board[index] != None:
            raise AlreadySelectedError("this case is already selected")

        self._board[index] = value
        self.__inverse_turns()

    def __inverse_turns(self):
        if self.turn == "O":
            self.turn = "X"
        elif self.turn == "X":
            self.turn = "O"

    def check_saturation(self):
        for index, value in self._board.items():
            if value == None:
                return False
        return True

    def check_winer(self):
        for combinaison in self._win_combinaisons:
            value = self.check_combinaison(combinaison)
            if value != False:
                return value, combinaison
        return False

    def check_combinaison(self, combinaison):
        if self._board[combinaison[0]] == None:
            return False
        else:
            if self._board[combinaison[0]] != self._board[combinaison[1]]:
                return False
            else:
                if self._board[combinaison[0]] != self._board[combinaison[2]]:
                    return False
                else:
                    return self._board[combinaison[0]]
