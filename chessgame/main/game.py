"""
Game Manager
"""

import time

from pawn import Pawn
from save import Save
from consts import COLOR_BLACK
from consts import COLOR_WHITE


class Game:
    """
    Game Manager
    """

    def __init__(self, game_mode):
        """
        Constructor
        Initiates game modes
        """
        self.end_game = False
        self.game_mode = game_mode
        self.figures = None
        self.saved = False
        print("\n\n")
        if game_mode == "ki":
            self.start_ai_game()
        elif game_mode == "m":
            self.start_multiplayer_game()
        else:
            while True:
                print("Welche Speicherdatei möchtest du laden? (Zurück mit b)")
                save_file = input("Eingabe: ")
                if save_file == "b":
                    return
                save_object = Save(save_file=save_file, game_object=None)
                save_load = save_object.load_game()
                if save_load is not None:
                    self.figures = save_load[1]
                    if save_load[0] == "m":
                        self.game_mode = "m"
                        self.start_multiplayer_game()
                        break
                    else:
                        self.game_mode = "ki"
                        self.start_ai_game()
                        break

    def start_multiplayer_game(self):
        """
        Instantiates multiplayer game:
        --> uses save file if not None
        --> Manages score and turn changes
        --> Saves and updates display after every turn

        Argument: figures from saved game state
        """
        print("Starte mehrspieler Spiel...")
        time.sleep(1.5)
        if self.figures is None:
            self.figures = []
            print("\nBaue Spielfeld auf...")
            time.sleep(1.5)
            for counter in range(8):
                self.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
                self.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
        print("\nWeiß Beginnt, Schwarz gew...wir werdens sehen ;)\n")
        time.sleep(1.5)
        player = "Weiß"
        while not self.end_game:
            self.update_display()
            print(f"\nSpieler {player} ist am Zug. (Auswahl A1, Beenden x, Speichern s)")
            user_input = input("Eingabe: ")
            if user_input == "s":
                Save(game_object=self, save_file=None)
                self.saved = True
                break
            elif user_input == "x":
                if self.saved:
                    print("\nBeende mehrspieler Spiel...")
                    time.sleep(1)
                    self.end_game = True
                else:
                    print("Möchtest du vor dem beenden deinen Spielstand speichern?\nSpeichern 's', Beenden 'x'")
                    save_input = input("Eingabe: ")
                    while True:
                        if save_input == "s":
                            Save(game_object=self, save_file=None)
                            self.saved = True
                            break
                        elif save_input == "x":
                            self.end_game = True
                            return
            else:
                figure = self.get_figure(user_input)
                self.saved = False
                if figure is None:
                    print("Falsche Eingabe. Bitte verwende das richtige Format (Bsp A4).\n")
                elif figure.color == COLOR_WHITE and player == "Schwarz" or figure.color == COLOR_BLACK and player == "Weiß":
                    print("Du kannst nicht die Figuren deines Gegners steuern.")
                else:
                    player = self.move_handler(figure, player, user_input)

    def start_ai_game(self):
        """
        Instantiates game against artificial intelligence:
        --> uses save file if not None
        --> Manages score
        --> Saves and updates display after ever turn

        Argument: figures from saved game state
        """
        print("Starte Spiel gegen KI...")
        time.sleep(1)
        if self.figures is None:
            print("Baue Spielfeld auf...")
            time.sleep(1)
            for counter in range(8):
                self.figures.append(Pawn(counter + 1, 1, COLOR_WHITE))
                self.figures.append(Pawn(counter + 1, 8, COLOR_BLACK))
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

        Return:
            player --> either white or black, changes after each turn
        """

        move_vector = {
            "m"  : {"x" :  0, "y" : 1},
            "m2" : {"x" :  0, "y" : 2},
            "l"  : {"x" : -1, "y" : 1},
            "r"  : {"x" :  1, "y" : 1}
        }

        while True:
            # Checks if the figure is in starting position
            if (figure.pos_y == 2 and figure.color == COLOR_WHITE) or (figure.pos_y == 7 and figure.color == COLOR_BLACK):
                starting_position = True
                print("\nWas möchtest du tun?\n2 Felder Vorwärts(m2), Vorwärts(m), Links(l), Rechts(r), Zurück(b)")
            else:
                starting_position = False
                print("\nWas möchtest du tun?\nVorwärts(m), Links(l), Rechts(r), Zurück(b)")

            move_input = input("Eingabe: ").lower()

            # Sets the right sign for the movement schemes
            if player == "Weiß":
                sign = 1
            else:
                sign = -1

            if move_input in move_vector:
                new_x = figure.pos_x + move_vector[move_input]["x"]
                new_y = figure.pos_y + move_vector[move_input]["y"] * sign      # *sign -> right direction for black or white

                target_occupied = self.is_occupied(new_x, new_y)

                if move_input == "m2" and target_occupied is None:
                    target_occupied = self.is_occupied(figure.pos_x + move_vector["m"]["x"], figure.pos_y + move_vector["m"]["y"] * sign)

                if (move_input == "m2" and starting_position) or move_input != "m2":
                    response = figure.move_to(new_x, new_y, target_occupied)

                    if response == 1:
                        self.check_for_hit(new_x, new_y, player)
                        figure.pos_x = new_x
                        figure.pos_y = new_y
                        break
                    elif response == 0:
                        print(f"Fehler: Zug {move_input} für {user_input} konnte nicht durgeführt werden.")
                    elif response == 2:
                        self.win(player)
                        break

                else:
                    print("m2 nicht zulässig.\n")

            elif move_input == "b":
                return player

            else:
                print("Falsche Eingabe.\n")

        # changes turn
        if player == "Weiß":
            return "Schwarz"
        return "Weiß"

    def check_for_hit(self, pos_x, pos_y, color):
        """
        gets coordinates from figure which made the move
        checks if it hit an enemy figure and removes it if so
        """
        figure = self.get_figure(f"{pos_x}::{pos_y}")
        if figure is None:
            return
        if color == "Weiß" and figure.color == COLOR_BLACK:
            self.figures.remove(figure)
            print("Weißer Bauer schlägt schwarzen Bauer.")
        elif color == "Schwarz" and figure.color == COLOR_WHITE:
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
                if figure.pos_x == int(pos[0]) and figure.pos_y == int(pos[1]):
                    return figure
        # user_input filter
        if len(user_input) != 2 or not user_input[1].isdigit() or int(user_input[1]) > 8:
            return None

        # uses ASCII table to convert Character to expected number
        converted_pos_x = ord(user_input[0].upper()) - ord("A") + 1

        if converted_pos_x < 1 or converted_pos_x > 8:
            return None

        for _, figure in enumerate(self.figures):
            if figure.pos_x == converted_pos_x and figure.pos_y == int(user_input[1]):
                return figure
        return None

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
        for _ in range(64):
            table.append("_")

        # fills table array with figure positions
        for _, figure in enumerate(self.figures):
            # transforms 2D array to 1D
            table[63-figure.pos_y*8+figure.pos_x] = figure.color

        table_output = "\n\n\n   A  B  C  D  E  F  G  H\n8  "
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
        table_output += "   A  B  C  D  E  F  G  H"
        print(table_output)
