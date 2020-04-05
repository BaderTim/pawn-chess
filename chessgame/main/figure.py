"""
Figure base class for the chess game
"""


class Figure:
    """
    Figure base class for the chess game
    """

    def __init__(self, pos_x, pos_y, color):
        """
        Constructor

        Args:
            pos_x {int}: start pos of pawn
            pos_y {int}: start pos of pawn
            color {String}: COLOR_BLACK or COLOR_WHITE
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def get_position(self):
        """
        Get position as tuple

        Return:
            Position {tuple}: (x, y)
        """
        return (self.pos_x, self.pos_y)

    def set_position(self, new_x, new_y):
        """
        Sets new position

        Args:
            new_x {int}: New x-coordinate for the figure
            new_y {int}: New y-coorinate for the figure
        """
        self.pos_x = new_x
        self.pos_y = new_y

    def get_pos_x(self):
        """
        Get x position

        Return:
            pos_x {int}: current x-coordinate of the figure
        """
        return self.pos_x

    def set_pos_x(self, new_x):
        """
        Sets new x position

        Args:
            new_x {int}: New x-coordinate for the figure
        """
        self.pos_x = new_x

    def get_pos_y(self):
        """
        Get y position

        Return:
            pos_Y {int}: current y-coordinate of the figure
        """
        return self.pos_y

    def set_pos_y(self, new_y):
        """
        Sets new y position

        Args:
            new_y {int}: New y-coordinate for the figure
        """
        self.pos_y = new_y

    def get_color(self):
        """
        Gets the color of the Figure

        Return:
            color {String}: Color of the figure
        """
        return self.color
