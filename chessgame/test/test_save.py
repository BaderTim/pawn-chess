#pylint: disable=C
import unittest
from chessgame.main.save import Save
from chessgame.main.consts import COLOR_BLACK, COLOR_WHITE, MODE_TEST, ACT_LOAD
from chessgame.main.pawn import Pawn
from chessgame.main.game import Game
import chessgame.test.test_game_std as std

class SaveTest(unittest.TestCase):

    def test_save_game(self):
        game = Game(MODE_TEST)
        game.start_game(MODE_TEST)
        std.stub_stdouts(self)
        std.stub_stdin(self, "test_file")
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))      
        save = Save(game, None)
        save.save_game() 
        file = open(save.path + save.save_file, "r")
        self.assertEqual(game.game_mode + "\n", file.readline())
        for counter, figure in enumerate(game.figures):
            self.assertEqual((f"{figure.color}_{figure.pos_x}#{figure.pos_y}\n"), file.readline())
        
        file.close()

        testlist = []
        test_game_mode = MODE_TEST
        for counter in range(8):
            testlist.append(Pawn(counter + 1, 2, COLOR_WHITE))
            testlist.append(Pawn(counter + 1, 7, COLOR_BLACK))
        
        del game
        self.doCleanups()
        std.stub_stdin(self, "test_file")
        game = Game(ACT_LOAD)
        for idx, figure in enumerate(testlist, 0):
            self.assertEqual(game.figures[idx].to_string(), figure.to_string())
        self.assertEqual(game.game_mode, test_game_mode)
