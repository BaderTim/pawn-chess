#pylint: disable=C
import unittest
from chessgame.main.save import Save
from chessgame.main.consts import COLOR_BLACK, COLOR_WHITE
from chessgame.main.pawn import Pawn
from chessgame.main.game import Game
import chessgame.test.test_game_std as std
class SaveTest(unittest.TestCase):
    def test_save_game(self):
        game = Game("test")
        game.start_game("test")
        std.stub_stdouts(self)
        std.stub_stdin(self, "test")
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))      
        save = Save(game, None)
        save.save_game() 
        file = open(save.path + save.save_file, "r")
        self.assertEqual(game.game_mode + "\n", file.readline())
        for counter, figure in enumerate(game.figures):
            self.assertEqual((f"{figure.color}_{figure.pos_x}#{figure.pos_y}\n"), file.readline())