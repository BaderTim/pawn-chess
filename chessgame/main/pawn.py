"""
Pawn figure for the chess game
"""
from chessgame.main.figure import Figure
from chessgame.main.consts import COLOR_BLACK, COLOR_WHITE


class Pawn(Figure):
    """
    Pawn figure for the chess game
    """

    def check_move_result(self, new_x, new_y, is_occupied):
        """
        Checks whether move can be made

        Args:
            new_x {int}: new position
            new_y {int}: new position
            is_occupied {None or COLOR}: is new position occupied?

        Return:
            response {int}:
                0 if move can not be made
                1 if move can be made
                2 if game will be won
        """

        if self.color == COLOR_WHITE:
            sign = 1
            finishing_row = 8
            opponent = COLOR_BLACK
        else:
            sign = -1
            finishing_row = 1
            opponent = COLOR_WHITE

        # moving forward if not occupied
        if self.pos_x == new_x and self.pos_y + 1 * sign == new_y and new_y == finishing_row and is_occupied is None:
            return 2
        if self.pos_x == new_x and self.pos_y + 1 * sign == new_y and is_occupied is None:
            return 1
        # moving 2 fields forward if not occupied
        if self.pos_x == new_x and self.pos_y + 2 * sign == new_y and is_occupied is None:
            return 1
        # left diagonal hit
        if self.pos_x - 1 == new_x and self.pos_y + 1 * sign == new_y and is_occupied == opponent:
            return 1
        # right diagonal hit
        if self.pos_x + 1 == new_x and self.pos_y + 1 * sign == new_y and is_occupied == opponent:
            return 1
        return 0

    def to_string(self):
        """
        Converts all data of the Pawn to a string

        Returns:
            pawn_string {String}: all relevant data of the pawn
        """
        return f"Position: x = {self.pos_x} , y = {self.pos_y}\nColor: {self.color}"
