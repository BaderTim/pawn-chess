"""
Figure base class for the chess game
"""


class Figure:
    """
    Figure base class for the chess game
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
        """
        Get position as tuple

        Return:
            Position as tuple (x, y)
        """
        return (self.pos_x, self.pos_y)

    def set_position(self, new_x, new_y):
        """
        Sets new position
        """
        self.pos_x = new_x
        self.pos_y = new_y

    def get_pos_x(self):
        """
        Get x position

        Return:
            x position
        """
        return self.pos_x

    def set_pos_x(self, new_x):
        """
        Sets new x position
        """
        self.pos_x = new_x

    def get_pos_y(self):
        """
        Get y position

        Return:
            y position
        """
        return self.pos_y

    def set_pos_y(self, new_y):
        """
        Sets new y position
        """
        self.pos_y = new_y

    def get_color(self):
        """
        Gets the color of the Figure

        Return:
            COLOR_BLACK or COLOR_WHITE
        """
        return self.color
