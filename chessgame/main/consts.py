"""
Consts for chess game
"""

GAME_SIZE = 8

COLOR_WHITE = "w"
COLOR_BLACK = "b"

PLAYER_WHITE = "Weiß"
PLAYER_BLACK = "Schwarz"

MODE_AI = "ai"
MODE_MULTI = "m"
MODE_TEST = "t"

ACT_NEW = "n"
ACT_LOAD = "l"
ACT_STOP = "x"
ACT_BACK = "b"
ACT_SAVE = "s"

MV_FWD1 = "m"
MV_FWD2 = "m2"
MV_LEFT = "l"
MV_RIGHT = "r"

COORD_X = "x"
COORD_Y = "y"

MOVE_VECTOR = {
    MV_FWD1  : {COORD_X :  0, COORD_Y : 1},
    MV_FWD2  : {COORD_X :  0, COORD_Y : 2},
    MV_LEFT  : {COORD_X : -1, COORD_Y : 1},
    MV_RIGHT : {COORD_X :  1, COORD_Y : 1}
}
