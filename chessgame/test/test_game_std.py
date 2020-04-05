# pylint: disable=C

import sys
import io
import unittest
import chessgame.main.consts as consts
from chessgame.main.game import Game
from chessgame.main.pawn import Pawn

def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = StringIO(inputs)


def stub_stdouts(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = StringIO()
    sys.stdout = StringIO()


class StringIO(io.StringIO):
    def __init__(self, value=''):
        value = value.encode('utf8', 'backslashreplace').decode('utf8')
        io.StringIO.__init__(self, value)

    def write(self, msg):
        io.StringIO.write(self, msg.encode(
            'utf8', 'backslashreplace').decode('utf8'))


class StdioChessTestCase(unittest.TestCase):

    def test_move_handler_input_b(self):
        stub_stdin(self, "b")
        stub_stdouts(self)

        game = Game("test")
        game.figures = []
        f = Pawn(2, 2, consts.COLOR_WHITE)
        game.figures.append(f)
        
        self.assertEqual(game.move_handler(f, consts.PLAYER_WHITE, "b2"), consts.PLAYER_WHITE)

    def test_move_handler_input_invalid_move_r(self):
        stub_stdin(self, "r\nb") #Input r, Inp b
        stub_stdouts(self)

        game = Game("test")
        game.figures = []
        f = Pawn(2, 2, consts.COLOR_WHITE)
        game.figures.append(f)
        game.move_handler(f, consts.PLAYER_WHITE, "b2")

        output = sys.stdout.getvalue()
        self.assertIn("Fehler: Zug r für b2 konnte nicht durchgeführt werden.", output)

    def test_move_handler_input_valid_move_m(self):
        stub_stdin(self, "m")
        stub_stdouts(self)

        game = Game("test")
        game.figures = []
        f = Pawn(2, 2, consts.COLOR_WHITE)
        game.figures.append(f)
        
        self.assertEqual(game.move_handler(f, consts.PLAYER_WHITE, "b2"), consts.PLAYER_BLACK)

    def test_move_handler_input_valid_win_move(self):
        stub_stdin(self, "m")
        stub_stdouts(self)

        game = Game("test")
        game.figures = []
        f = Pawn(2, 7, consts.COLOR_WHITE)
        game.figures.append(f)
        
        self.assertEqual(game.move_handler(f, consts.PLAYER_WHITE, "b7"), consts.PLAYER_BLACK)
        output = sys.stdout.getvalue()
        self.assertIn("Spieler Weiß hat gewonnen!", output)

    def test_move_handler_input_invalid(self):
        stub_stdin(self, "test1234\nb") #Input test1234, Inp b
        stub_stdouts(self)

        game = Game("test")
        game.figures = []
        f = Pawn(2, 2, consts.COLOR_WHITE)
        game.figures.append(f)
        game.move_handler(f, consts.PLAYER_WHITE, "b2")

        output = sys.stdout.getvalue()
        self.assertIn("Falsche Eingabe.\n", output)

    def test_move_handler_input_invalid_move_m2(self):
        stub_stdin(self, "m2\nb") #Input m2 Inp b
        stub_stdouts(self)

        game = Game("test")
        game.figures = []
        f = Pawn(2, 3, consts.COLOR_WHITE)
        game.figures.append(f)
        game.move_handler(f, consts.PLAYER_WHITE, "b3")

        output = sys.stdout.getvalue()
        self.assertIn("m2 nicht zulässig.\n", output)

    def test_quit_game(self):
        stub_stdouts(self)
        game = Game("test")
        game.figures = []

        game.quit_game()

        output = sys.stdout.getvalue()
        self.assertIn("\nBeende das Spiel...", output)
        self.assertTrue(game.end_game)
    
    """
    def test_game_init_input_b(self):
        stub_stdin(self, "b")
        stub_stdouts(self)

        game = Game(consts.ACT_LOAD)

        #output = sys.stdout.getvalue()
        self.assertIsNone(game) 
    """