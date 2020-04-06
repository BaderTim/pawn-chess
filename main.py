"""
Main class
"""

import chessgame.main.consts as consts
from chessgame.main.game import Game


def main():
    """
    Main Menu

    User can select between different game modes
    or load a saved game

    Returns:
        test_result {int}:
            0 new game has been started
            1 Game has been stopped in mode selection
            2 Game went back to the main menu from load menu
            3 Game has been stopped from main menu
    """
    while True:
        print("\n\n\n---WELCOME TO BAUERNSCHACH---\n")
        print("Neues Spiel: n\nSpiel laden: l\nBeenden: x\n")
        user_input = input("Eingabe: ").lower()
        if user_input == consts.ACT_NEW:
            print("\n\n\n # Neues Spiel # \nGegen Computer: ki\nMehrspieler: m\nZurück: b\n")
            game_mode = input("Eingabe: ").lower()
            if game_mode in (consts.MODE_AI, consts.MODE_MULTI):
                Game(game_mode)
                return 0
            if game_mode == consts.ACT_STOP:
                return 1
            if game_mode != consts.ACT_BACK:
                print(f"Fehler: '{game_mode}' konnte nicht zugeordnet werden. Bitte versuche es erneut.")
        elif user_input == consts.ACT_LOAD:
            Game(consts.ACT_LOAD)
            return 2
        elif user_input == consts.ACT_STOP:
            return 3

if __name__ == '__main__':
    main()
