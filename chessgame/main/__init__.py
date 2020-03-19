"""
Main class
"""

from chessgame.main.game import Game


def main():
    """
    Main Menu

    User can select between different game modes
    or load a saved game
    """
    while True:
        print("\n\n\n---WELCOME TO BAUERNSCHACH---\n")
        print("Neues Spiel: n\nBeenden: x\n")
        user_input = input("Eingabe: ")
        if user_input == "n":
            print("\n\n\n # Neues Spiel # \nGegen Computer: ki\nMultiplayer: m\nSpiel laden: l\nZurück: b\n")
            game_mode = input("Eingabe: ")
            if game_mode in ("ki", "m", "l"):
                Game(game_mode)
            elif game_mode == "x":
                break
            elif game_mode != "b":
                print(f"Fehler: '{game_mode}' konnte nicht zugeordnet werden. Bitte versuche es erneut.")
        elif user_input == "x":
            break


if __name__ == '__main__':
    main()
