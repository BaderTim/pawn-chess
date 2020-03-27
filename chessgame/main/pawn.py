"""Pawn figure for the chess game
"""

from figure import Figure


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
        if self.color == "w":
            # moving forward if not occupied
            if self.pos_y + 1 == new_y and new_y == 8 and is_occupied is None:      #Moved up here to fix win conditions
                return 2
            if self.pos_y + 1 == new_y and self.pos_x == new_x and is_occupied is None:
                return 1
            # moving 2 fields forward if not occupied
            if self.pos_y + 2 == new_y and self.pos_x == new_x and is_occupied is None:
                return 1
            # left diagonal hit
            if self.pos_x - 1 == new_x and self.pos_y + 1 == new_y and is_occupied == "b":
                return 1
            # right diagonal hit
            if self.pos_x + 1 == new_x and self.pos_y + 1 == new_y and is_occupied == "b":
                return 1

        # black pawns (top start)
        else:
            # moving forward if not occupied
            if self.pos_y - 1 == new_y and new_y == 1 and is_occupied is None:      #Moved up here to fix win conditions
                return 2
            if self.pos_y - 1 == new_y and self.pos_x == new_x and is_occupied is None:
                return 1
            # moving 2 fields forward if not occupied
            if self.pos_y - 2 == new_y and self.pos_x == new_x and is_occupied is None:
                return 1
            # left diagonal hit
            if self.pos_x - 1 == new_x and self.pos_y - 1 == new_y and is_occupied == "w":
                return 1
            # right diagonal hit
            if self.pos_x + 1 == new_x and self.pos_y - 1 == new_y and is_occupied == "w":
                return 1
        return 0
