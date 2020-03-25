"""
save file class
"""

from pawn import Pawn
import os


class Save:
    """
    save file class
    """

    def __init__(self, game_object, save_file):
        """
        Argument:
            save_file --> None if new save file
                      --> tries to load if given
            game_object --> Game object to save
        """
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\saved_files\\"

        # saves game_object data to new save file
        if save_file is None:
            print("Unter welchem Namen möchtest du die Datei speichern?")
            self.save_file = input("Eingabe: ")
            if ".txt" not in self.save_file:
                self.save_file += ".txt"
            self.game = game_object
            self.save_game()
        # loads save_file
        else:
            self.save_file = save_file
            if ".txt" not in self.save_file:
                self.save_file += ".txt"

    def load_game(self):
        """
        loads save file
        :returns game mode and figures
        """
        try:
            file = open(self.path+self.save_file, "r")
            file_lines = file.readlines()
            save_load = []
            figures = []
            for counter, line in enumerate(file_lines):
                if counter == 0:
                    if ("m" or "ki") not in line:
                        print(f"\nFehler: Datei '{self.save_file}' scheint "
                              f"einen fehlerhaften Spielmodi in Zeile {counter+1} zu haben.\n")
                        return None
                    save_load.append(line.replace("\n", ""))
                else:
                    data = line.replace(" ", "").replace("\n", "").split("_")
                    if data[0] != "w" and data[0] != "b":
                        print(f"\nFehler: Datei '{self.save_file}' scheint "
                              f"fehlerhafte Farben in Zeile {counter+1} zu haben.\n")
                        return None
                    cords = data[1].split("#")
                    if int(cords[0]) < 1 or int(cords[0]) > 8 or int(cords[1]) < 1 or int(cords[1]) > 8:
                        print(f"\nFehler: Datei '{self.save_file}' scheint "
                              f"fehlerhafte Koordinaten in Zeile {counter+1} zu haben.\n")
                        return None
                    figures.append(Pawn(pos_x=int(cords[0]), pos_y=int(cords[1]), color=data[0]))
            save_load.append(figures)
            return save_load
        except FileNotFoundError:
            print(f"\nFehler: konnte '{self.save_file}' nicht finden.\n")
        except TypeError:
            print(f"\nFehler: Datei '{self.save_file}' scheint fehlerhafte Koordinaten zu haben.")
        return None

    def save_game(self):
        """
        saves file
        """
        file = open(self.path+self.save_file, "w+")
        file.write(self.game.game_mode+"\n")
        for _, figure in enumerate(self.game.figures):
            file.write(f"{figure.color}_{figure.pos_x}#{figure.pos_y}\n")
        file.close()
        print(f"\nSpiel wurde unter '{self.save_file}' gespeichert.\n")
