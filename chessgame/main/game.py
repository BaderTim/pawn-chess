"""
Game Manager
"""

import random
import time
import chessgame.main.consts as consts
from chessgame.main.pawn import Pawn
from chessgame.main.save import Save


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
        self.ai_pawns = []
        self.saved = False
        print("\n\n")
        if game_mode == consts.MODE_KI:
            self.start_ai_game()
        elif game_mode == consts.MODE_MULTI:
            self.start_multiplayer_game()
        elif game_mode != "test":
            while True:
                print("Welche Speicherdatei möchtest du laden? (Zurück mit b)")
                save_file = input("Eingabe: ").lower()
                if save_file == consts.ACT_BACK:
                    return
                save_object = Save(save_file=save_file, game_object=None)
                save_load = save_object.load_game()
                if save_load is not None:
                    self.figures = save_load[1]
                    if save_load[0] == consts.MODE_MULTI:
                        self.game_mode = consts.MODE_MULTI
                        self.start_multiplayer_game()
                        break
                    self.game_mode = consts.MODE_KI
                    self.start_ai_game()
                    break

    def start_game(self, game_mode):
        """
        Starts beginning of the game
        """
        if game_mode == consts.MODE_MULTI:
            print("Starte mehrspieler Spiel...")
        else:
            print("Starte KI Spiel...")

        time.sleep(1.5)
        if self.figures is None or len(self.figures) == 0:
            self.figures = []
            print("\nBaue Spielfeld auf...")
            time.sleep(1.5)
            for counter in range(8):
                self.figures.append(Pawn(counter + 1, 2, consts.COLOR_WHITE))
                self.figures.append(Pawn(counter + 1, 7, consts.COLOR_BLACK))
        print("\nWeiß Beginnt, Schwarz gew...wir werdens sehen ;)\n")
        time.sleep(1.5)

    def save_game(self, user_input):
        """
        Handles saving and closing the game
        """
        if user_input == consts.ACT_SAVE:
            Save(game_object=self, save_file=None)
            self.saved = True
        if user_input == consts.ACT_STOP:
            if self.saved:
                print("\nBeende mehrspieler Spiel...")
                time.sleep(1)
                self.end_game = True
            else:
                print("Möchtest du vor dem beenden deinen Spielstand speichern?\nSpeichern 's', Beenden 'x'")
                save_input = input("Eingabe: ").lower()
                while True:
                    if save_input == consts.ACT_SAVE:
                        Save(game_object=self, save_file=None)
                        self.saved = True
                        self.end_game = True
                        break
                    if save_input == consts.ACT_STOP:
                        self.end_game = True
                        return

    def start_multiplayer_game(self):
        """
        Instantiates multiplayer game:
        --> uses save file if not None
        --> Manages score and turn changes
        --> Saves and updates display after every turn

        Argument: figures from saved game state
        """
        self.start_game(consts.MODE_MULTI)

        player = consts.PLAYER_WHITE
        while not self.end_game:
            self.update_display()
            print(f"\nSpieler {player} ist am Zug. (Auswahl z.B. A2, Beenden x, Speichern s)")
            user_input = input("Eingabe: ").lower()
            self.save_game(user_input)
            if user_input not in (consts.ACT_SAVE, consts.ACT_STOP):
                figure = self.get_figure(user_input)
                self.saved = False
                if figure is None:
                    print("Falsche Eingabe. Bitte verwende das richtige Format (Bsp A4).\n")
                elif (figure.color == consts.COLOR_WHITE and player == consts.PLAYER_BLACK or
                      figure.color == consts.COLOR_BLACK and player == consts.PLAYER_WHITE):
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
        self.start_game(consts.MODE_KI)

        player = consts.PLAYER_WHITE
        while not self.end_game:
            while player == consts.PLAYER_WHITE and not self.end_game:
                self.update_display()
                print(f"\nSpieler {player} ist am Zug. (Auswahl z.B. A2, Beenden x, Speichern s)")
                user_input = input("Eingabe: ").lower()
                self.save_game(user_input)
                if user_input not in (consts.ACT_SAVE, consts.ACT_STOP):
                    print(f"\nSpieler {player} ist am Zug.")
                    figure = self.get_figure(user_input)
                    self.saved = False
                    if figure is None:
                        print("Falsche Eingabe. Bitte verwende das richtige Format (Bsp A4).\n")
                    elif (figure.color == consts.COLOR_WHITE and player == consts.PLAYER_BLACK or
                          figure.color == consts.COLOR_BLACK and player == consts.PLAYER_WHITE):
                        print("Du kannst nicht die Figuren deines Gegners steuern.")
                    else:
                        player = self.move_handler(figure, player, user_input)

            # AI Move
            while player == consts.PLAYER_BLACK and not self.end_game:
                self.update_display()
                self.update_ai_pawns()
                print(f"\nSpieler {player} ist am Zug.")

                possible_ai_moves = self.ai_moves()
                best_possible_moves = []

                for movedict in possible_ai_moves.items():
                    best_possible_moves.append(self.get_best_move(movedict))

                final_decision = self.ai_decide(best_possible_moves)

                figure = self.get_figure(final_decision[0])
                player = self.move_handler(figure, player, f"{figure.pos_x}::{figure.pos_y}", final_decision[1])
                time.sleep(1)

    def move_handler(self, figure, player, user_input, move_input=None):
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
        while True:
            # Checks if the figure is in starting position
            starting_position = ((figure.get_pos_y() == 2 and figure.color == consts.COLOR_WHITE) or
                                 (figure.get_pos_y() == 7 and figure.color == consts.COLOR_BLACK))

            if move_input is None:
                self.print_move_options(starting_position)
                move_input = input("Eingabe: ").lower()

            if move_input == consts.ACT_BACK:
                return player


            response = self.make_move(figure, player, move_input, starting_position)

            if response == 0:
                print(f"Fehler: Zug {move_input} für {user_input} konnte nicht durchgeführt werden.")
            elif response == 1:
                break
            if response == 2:
                self.win(player)
                break
            if response == 3:
                print("Falsche Eingabe.\n")
            elif response == 4:
                print("m2 nicht zulässig.\n")

            move_input = None
        return self.toggle_player(player)

    def make_move(self, figure, player, move_input, starting_position):
        """
        Makes Move
        """
        move_vector = {
            consts.MV_FWD1  : {consts.COORD_X :  0, consts.COORD_Y : 1},
            consts.MV_FWD2  : {consts.COORD_X :  0, consts.COORD_Y : 2},
            consts.MV_LEFT  : {consts.COORD_X : -1, consts.COORD_Y : 1},
            consts.MV_RIGHT : {consts.COORD_X :  1, consts.COORD_Y : 1}
        }
        # invalid input
        if move_input not in move_vector:
            return 3

        # Sets the right sign for the movement schemes
        sign = 1
        if player == consts.PLAYER_BLACK:
            sign = -1

        new_x = figure.get_pos_x() + move_vector[move_input][consts.COORD_X]
        new_y = figure.get_pos_y() + move_vector[move_input][consts.COORD_Y] * sign      # *sign -> right direction for black or white

        target_occupied = self.is_occupied(new_x, new_y)

        if move_input == consts.MV_FWD2 and target_occupied is None:
            target_occupied = self.is_occupied(figure.get_pos_x() + move_vector[consts.MV_FWD1][consts.COORD_X],
                                               figure.get_pos_y() + move_vector[consts.MV_FWD1][consts.COORD_Y] * sign)

        if (move_input == consts.MV_FWD2 and starting_position) or move_input != consts.MV_FWD2:
            response = figure.move_to(new_x, new_y, target_occupied)

            if response == 1:
                self.check_for_hit(new_x, new_y, player)
                figure.set_pos_x(new_x)
                figure.set_pos_y(new_y)
                self.check_last_figure(player)

        # m2 not allowed
        else:
            return 4

        return response

    def check_for_hit(self, pos_x, pos_y, color):
        """
        gets coordinates from figure which made the move
        checks if it hit an enemy figure and removes it if so
        """
        figure = self.get_figure(f"{pos_x}::{pos_y}")
        if figure is None:
            return
        if color == consts.PLAYER_WHITE and figure.color == consts.COLOR_BLACK:
            self.figures.remove(figure)
            print("Weißer Bauer schlägt schwarzen Bauer.\n")
        elif color == consts.PLAYER_BLACK and figure.color == consts.COLOR_WHITE:
            self.figures.remove(figure)
            print("Schwarzer Bauer schlägt weißen Bauer.\n")

    def win(self, color):
        """
        Stops game thread by exiting main loop
        selects color as winner
        """
        self.update_display()
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
                if figure.get_pos_x() == int(pos[0]) and figure.get_pos_y() == int(pos[1]):
                    return figure
        # user_input filter
        if len(user_input) != 2 or not user_input[1].isdigit() or int(user_input[1]) > 8:
            return None

        # uses ASCII table to convert Character to expected number
        converted_pos_x = ord(user_input[0].upper()) - ord("A") + 1

        if converted_pos_x < 1 or converted_pos_x > 8:
            return None

        for _, figure in enumerate(self.figures):
            if figure.get_pos_x() == converted_pos_x and figure.get_pos_y() == int(user_input[1]):
                return figure
        return None

    def update_ai_pawns(self):
        '''
        Updates pawns of the AI player
        '''
        self.ai_pawns = []
        for figure in self.figures:
            if figure.color == consts.COLOR_BLACK:
                self.ai_pawns.append(figure)

    def ai_moves(self):
        '''
        Returns a dict with all possible moves and their confidence values [0;100]
        '''
        self.update_ai_pawns()
        possible_moves = {}

        for pawn in self.ai_pawns:
            templist = {}
            # List of next position after each possible move: new_pos ['m','m2','l','r']
            new_pos = [[pawn.get_pos_x(), pawn.get_pos_y()-1], [pawn.get_pos_x(), pawn.get_pos_y()-2],
                       [pawn.get_pos_x()-1, pawn.get_pos_y()-1], [pawn.get_pos_x()+1, pawn.get_pos_y()-1]]

            # Assigning confidence values | 0 == impossible ; 100 = winning move
            if pawn.get_pos_y() == 7 and self.is_occupied(new_pos[1][0], new_pos[1][1]) is None and self.is_occupied(new_pos[1][0], new_pos[1][1] + 1) is None:
                templist.update({consts.MV_FWD2: (100 / new_pos[1][1])})
            else:
                templist.update({consts.MV_FWD2: 0})

            if self.is_occupied(new_pos[0][0], new_pos[0][1]) is None:
                templist.update({consts.MV_FWD1: (100/new_pos[0][1])})
            else:
                templist.update({consts.MV_FWD1:0})

            if self.is_occupied(new_pos[2][0], new_pos[2][1]) == consts.COLOR_WHITE:
                templist.update({consts.MV_LEFT: (100 / new_pos[2][1]) + 20})
            else:
                templist.update({consts.MV_LEFT: 0})

            if self.is_occupied(new_pos[3][0], new_pos[3][1]) == consts.COLOR_WHITE:
                templist.update({consts.MV_RIGHT: (100 / new_pos[3][1]) + 20})
            else:
                templist.update({consts.MV_RIGHT: 0})

            possible_moves.update({f'{pawn.get_pos_x()}::{pawn.get_pos_y()}':templist})

        return possible_moves

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

    def check_last_figure(self, player):
        '''
        Checks if the last captured figure was the last of the opponent
        '''
        counter_figures = 0
        for _, pawn in enumerate(self.figures, 1):
            if player == consts.PLAYER_WHITE:
                enemy_color = consts.COLOR_BLACK
            else:
                enemy_color = consts.COLOR_WHITE

            if pawn.color == enemy_color:
                counter_figures += 1

        if counter_figures <= 0:
            self.win(player)

    @staticmethod
    def ai_decide(movelist: list):
        '''
        Decides which move will be executed based on confidence values
        '''
        max_val = 0
        i = len(movelist) -1
        for move in movelist:
            if move[2] > max_val:
                max_val = move[2]
        while i >= 0:
            if movelist[i][2] < max_val:
                movelist.pop(i)
            i -= 1
        if len(movelist) > 1:
            return movelist[random.randint(0, len(movelist)-1)]
        return movelist[0]

    @staticmethod
    def get_best_move(movedict):
        '''
        gets the best possible move for a specific pawn
        '''
        max_key = max(movedict[1], key=lambda k: movedict[1][k])
        ret_val = [movedict[0], max_key, movedict[1][max_key]]
        return ret_val

    @staticmethod
    def toggle_player(player):
        """
        changes turn
        """
        if player == consts.PLAYER_WHITE:
            return consts.PLAYER_BLACK
        return consts.PLAYER_WHITE

    @staticmethod
    def print_move_options(starting_position):
        """
        output of move options
        """
        text = "\nWas möchtest du tun?\n"
        if starting_position:
            text += "2 Felder Vorwärts(m2), "
        text += "Vorwärts(m), Links(l), Rechts(r), Zurück(b)"
        print(text)
