"""
Game Manager
"""

from chessgame.main.figure import Figure
from chessgame.main.pawn import Pawn


class Game:
    """
    Game Manager
    """

    def __init__(self, gamemode):
        """
        Constructor
        Initiates game modes
        """
        self.end_game = False
        self.gamemode = gamemode
        self.figures = None
        if gamemode == "ki":
            self.start_ai_game()
        elif gamemode == "m":
            self.start_multiplayer_game()
        else:
            print("Versuche gespeichertes Spiel zu laden...")
            # TODO: load saved game --> get game mode and figures, launch game
            # self.figures = savedFigures...

    def start_multiplayer_game(self):
        """
        Instantiates multiplayer game:
        --> uses save file if not None
        --> Manages score and turn changes
        --> Saves and updates display after every turn

        Argument: figures from saved game state
        """
        print("Starte mehrspieler Spiel...")
        if self.figures is None:
            print("Baue Spielfeld auf...")
            for counter in range(8):
                self.figures.append(Pawn(Figure(counter + 1, 0, "w")))
                self.figures.append(Pawn(Figure(counter + 1, 8, "b")))
        print("Weiß Beginnt, Schwarz gew...wir werdens sehen ;)\n")
        player = "Weiß"
        while not self.end_game:
            self.update_display()
            user_input = input(f"Spieler {player} ist am Zug: ")
            if self.get_figure(user_input) is None:
                print("Falsche Eingabe. Bitte verwende das richtige Format (Bsp A4).\n")
            else:
                figure = self.get_figure(user_input)
                self.move_handler(figure, player, user_input)
                player = "Schwarz"
    def start_ai_game(self):
        """
        Instantiates game against artificial intelligence:
        --> uses save file if not None
        --> Manages score
        --> Saves and updates display after ever turn

        Argument: figures from saved game state
        """
        print("Starte Spiel gegen KI...")
        if self.figures is None:
            print("Baue Spielfeld auf...")
            for counter in range(8):
                self.figures.append(Pawn(Figure(counter + 1, 0, "w")))
                self.figures.append(Pawn(Figure(counter + 1, 8, "b")))
        self.update_display()
        # TODO: Ai interaction

    def move_handler(self, figure, player, user_input):
        """
        Arguments:
            figure --> selected figure
            player --> White or Black
            user_input --> raw user input for text response

        Function:
            handles movement of figures, e.g. wins and hits
        """
        while True:
            print("\nWas möchtest du tun?\nVorwärts(m), Links(l), Rechts(r)")
            move_input = input("Eingabe: ")
            
            if player is "Weiß":
                if move_input is "m":
                    response = figure.move_to(figure.pos_x, figure.pos_y+1, 
                                              self.is_occupied(figure.pos_x, figure.pos_y+1))
                    if response is 1:
                        self.check_for_hit(figure.pos_x, figure.pos_y+1, player)
                        break
                    elif response is 0:
                        print(f"Fehler: konnte {user_input} nicht nach vorne bewegen.")
                    elif response is 2:
                        self.win(player)
                        break
                        
                elif move_input is "r":
                    response = figure.move_to(figure.pos_x+1, figure.pos_y+1,
                                              self.is_occupied(figure.pos_x+1, figure.pos_y+1))
                    if response is 1:
                        self.check_for_hit(figure.pos_x+1, figure.pos_y+1, player)
                        break
                    elif response is 0:
                        print(f"Fehler: konnte {user_input} nicht nach rechts vorne bewegen.")
                    elif response is 2:
                        self.win(player)
                        break

                elif move_input is "l":
                    response = figure.move_to(figure.pos_x-1, figure.pos_y+1,
                                              self.is_occupied(figure.pos_x-1, figure.pos_y+1))
                    if response is 1:
                        self.check_for_hit(figure.pos_x-1, figure.pos_y+1, player)
                        break
                    elif response is 0:
                        print(f"Fehler: konnte {user_input} nicht nach links vorne bewegen.")
                    elif response is 2:
                        self.win(player)
                        break
                else:
                    print("Falsche Eingabe.\n")
                    
            else:
                if move_input is "m":
                    response = figure.move_to(figure.pos_x, figure.pos_y-1,
                                              self.is_occupied(figure.pos_x, figure.pos_y-1))
                    if response is 1:
                        self.check_for_hit(figure.pos_x, figure.pos_y-1, player)
                        break
                    elif response is 0:
                        print(f"Fehler: konnte {user_input} nicht nach vorne bewegen.")
                    elif response is 2:
                        self.win(player)
                        break

                elif move_input is "r":
                    response = figure.move_to(figure.pos_x+1, figure.pos_y-1,
                                              self.is_occupied(figure.pos_x+1, figure.pos_y-1))
                    if response is 1:
                        self.check_for_hit(figure.pos_x+1, figure.pos_y-1, player)
                        break
                    elif response is 0:
                        print(f"Fehler: konnte {user_input} nicht nach rechts vorne bewegen.")
                    elif response is 2:
                        self.win(player)
                        break

                elif move_input is "l":
                    response = figure.move_to(figure.pos_x-1, figure.pos_y-1,
                                              self.is_occupied(figure.pos_x-1, figure.pos_y-1))
                    if response is 1:
                        self.check_for_hit(figure.pos_x-1, figure.pos_y-1, player)
                        break
                    elif response is 0:
                        print(f"Fehler: konnte {user_input} nicht nach links vorne bewegen.")
                    elif response is 2:
                        self.win(player)
                        break
                else:
                    print("Falsche Eingabe.\n")      
        
    def check_for_hit(self, pos_x, pos_y, color):
        """
        gets coordinates from figure which made the move
        checks if it hit an enemy figure and removes it if so
        """
        figure = self.get_figure(f"{pos_x}::{pos_y}")
        if color is "Weiß" and figure.color is "b":
            self.figures.remove(figure)
            print("Weißer Bauer schlägt schwarzen Bauer.")
        elif color is "Schwarz" and figure.color is "w":
            self.figures.remove(figure)
            print("Schwarzer Bauer schlägt weißen Bauer.")

    def win(self, color):
        """
        Stops game thread by exiting main loop
        selects color as winner
        """
        print(f"Spieler {color} hat gewonnen!")
        self.end_game = True

    def is_occupied(self, pos_x, pos_y):
        """
        Arguments:
             pos_x as int
             pos_y as int

        Returns:
            color if figure is existent
            otherwise None
        """
        figure = self.get_figure(f"{pos_x}::{pos_y}")
        if figure is not None:
            return figure.color
        return None

    def get_figure(self, user_input):
        """
        Arguments: self, coordinates from user interaction as string
                    alternative user_input comes with '::' in the middle,
                        used by is_occupied and check_for_hit method with exact coordinates
        :return figure if found, otherwise None
        """

        # alternative use by is_occupied() and check_for_hit()
        if "::" in user_input:
            pos = user_input.split("::")
            for _, figure in enumerate(self.figures):
                if figure.pos_x == pos[0] and figure.pos_y == int(pos[1]):
                    return figure
        # user_input filter
        pos = user_input.split("")
        if len(pos) != 2 or not pos[1].isdigit() or int(pos[1]) > 8:
            return None
        if pos[0] == "A" or pos[0] == "a":
            pos[0] = 1
        elif pos[0] == "B" or pos[0] == "b":
            pos[0] = 2
        elif pos[0] == "C" or pos[0] == "c":
            pos[0] = 3
        elif pos[0] == "D" or pos[0] == "d":
            pos[0] = 4
        elif pos[0] == "E" or pos[0] == "e":
            pos[0] = 5
        elif pos[0] == "F" or pos[0] == "f":
            pos[0] = 6
        elif pos[0] == "G" or pos[0] == "g":
            pos[0] = 7
        elif pos[0] == "H" or pos[0] == "h":
            pos[0] = 8
        else:
            return None
        for _, figure in enumerate(self.figures):
            if figure.pos_x == pos[0] and figure.pos_y == int(pos[1]):
                return figure


    def update_display(self):
        """
        Updates Graphic Display

        Argument: array with figure objects

        Function:
            -generates 1d table array
            -fills array with figures
            -outputs array to console
        """
        table = []
        # generates table array --> 1D array to describe chess field
        for counter in range(64):
            table.append("_")

        # fills table array with figure positions
        for _, figure in enumerate(self.figures):
            # TODO: Transform 2D to 1D, the following line is corrupted
            table[(8 - figure.pos_y) * 8 + figure.pos_x] = figure.color

        table_output = "   A  B  C  D  E  F  G  H\n8  "
        line_space = 0
        coordinate_system_y = 8
        # builds output string in form of a chess field
        for _, pos in enumerate(table):
            table_output += f"{pos}  "
            line_space += 1
            # creates a line space after every 8 fields
            if line_space == 8:
                left_side_y = coordinate_system_y - 1
                if left_side_y > 0:
                    table_output += f" {coordinate_system_y}\n{left_side_y}  "
                else:
                    table_output += f" {coordinate_system_y}\n"
                coordinate_system_y -= 1
                line_space = 0
        table_output += "\n   A  B  C  D  E  F  G  H"
        print(table_output)
