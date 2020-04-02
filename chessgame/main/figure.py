"""
Figure base class for the chess game
"""


class Figure:
    """Figure base class for the chess game
    """

    def __init__(self, pos_x, pos_y, color):
        """
        Arguments:
            pos_x {int} -- start pos of pwan
            pos_y {int} -- start pos of pwan
            color {String} -- COLOR_BLACK or COLOR_WHITE
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def get_position(self):
        """Get position as tuple

        Return:
            Position as tuple (x, y)
        """
        return (self.pos_x, self.pos_y)

    def get_color(self):
        """Gets the color of the Figure

        Return:
            COLOR_BLACK or COLOR_WHITE
        """
        return self.color
