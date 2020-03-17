from chessgame.main.game import Game



def main():
    """
    Main Menu

    User can select between different game modes
    or load a saved game
    """
    while True:
        print("\n---WELCOME TO BAUERNSCHACH---\n")
        print("Neues Spiel: 'n'\nBeenden: x\n")
        user_input = input("Eingabe: ")
        if user_input == "n":
            print("\n # Neues Spiel # \nGegen Computer: 'ki'\nMultiplayer: 'm'\nSpiel laden: 'l'\nZurück: 'b'\n")
            gamemode = input("Eingabe: ")
            if gamemode == "ki" or gamemode == "m" or gamemode == "l":
                game(gamemode)
            elif gamemode == "x":
                break
            elif gamemode != "b":
                print(f"Fehler: '{gamemode}' konnte nicht zugeordnet werden. Bitte versuche es erneut.")
        elif user_input == "x":
            break


if __name__ == '__main__':
    main()