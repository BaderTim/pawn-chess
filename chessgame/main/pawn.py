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
            True if move was made
            False if move could not be made
        """

        # white pawns
        if self.color is "w":
            # moving forward if not occupied
            if self.pos_y + 1 is new_y and self.pos_x is new_x and is_occupied is None:
                return True
            # left diagonal hit
            if self.pos_x - 1 is new_x and self.pos_y + 1 is new_y and is_occupied is "b":
                # TODO: Hit
                return True
            # right diagonal hit
            if self.pos_x + 1 is new_x and self.pos_y + 1 is new_y and is_occupied is "b":
                # TODO: Hit
                return True

        # black pawns
        else:
            # moving forward if not occupied
            if self.pos_y - 1 is new_y and self.pos_x is new_x and is_occupied is None:
                return True
            # left diagonal hit
            if self.pos_x - 1 is new_x and self.pos_y - 1 is new_y and is_occupied is "w":
                # TODO: Hit
                return True
            # right diagonal hit
            if self.pos_x + 1 is new_x and self.pos_y - 1 is new_y and is_occupied is "w":
                # TODO: Hit
                return True
