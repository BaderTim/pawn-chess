"""Pawn figure for the chess game
"""

from chessgame.main.figure import Figure


class Pawn(Figure):
    """Pawn figure for the chess game
    """

    def move_to(self, new_x, new_y, is_occupied):
        """
        Move figure to new position

        Arguments:
            new_x {int} -- new position
            new_y {int} -- new position
            is_occupied {None or COLOR} -- is new position occupied?

        Return:
            0 if move was not made
            1 if move has been made
            2 if game has been won
        """

        # white pawns (bottom start)
        if self.color is "w":
            # moving forward if not occupied
            if self.pos_y + 1 is new_y and self.pos_x is new_x and is_occupied is None:
                return 1
            # left diagonal hit
            if self.pos_x - 1 is new_x and self.pos_y + 1 is new_y and is_occupied is "b":
                return 1
            # right diagonal hit
            if self.pos_x + 1 is new_x and self.pos_y + 1 is new_y and is_occupied is "b":
                return 1
            if self.pos_y + 1 is new_y and new_y > 8:
                return 2

        # black pawns (top start)
        else:
            # moving forward if not occupied
            if self.pos_y - 1 is new_y and self.pos_x is new_x and is_occupied is None:
                return 1
            # left diagonal hit
            if self.pos_x - 1 is new_x and self.pos_y - 1 is new_y and is_occupied is "w":
                return 1
            # right diagonal hit
            if self.pos_x + 1 is new_x and self.pos_y - 1 is new_y and is_occupied is "w":
                return 1
            if self.pos_y - 1 is new_y and new_y < 1:
                return 2
        return 0
