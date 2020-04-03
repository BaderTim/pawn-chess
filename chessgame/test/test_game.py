import unittestACT_STOP
from chessgame.main.game import Game
from chessgame.main.consts import MODE_MULTI
from chessgame.main.consts import COLOR_BLACK
from chessgame.main.consts import COLOR_WHITE
from chessgame.main.consts import ACT_SAVE
from chessgame.main.consts import ACT_STOP
from chessgame.main.pawn import Pawn

class GameTest(unittest.TestCase):
    '''
        Testclass for Game
    '''
    def test_start_game(self):
        '''
        Test for game.start_game
            - tests if the array is produced correctly
        '''
        game = Game(MODE_MULTI)
        pawns = []
        for counter in range(8):
            pawns.append(Pawn(counter + 1, 2, COLOR_WHITE))
            pawns.append(Pawn(counter + 1, 7, COLOR_BLACK))
        game.start_game(game.game_mode)
        self.assertEqual(len(pawns), len(game.figures))
        self.assertEqual(len(game.figures), 16)
        for counter in range(16):
            self.assertEqual(game.figures[counter].get_position, pawns[counter].get_position)

    def test_save_game(self):
        '''
        Test for game.same_game
        '''
        game = Game(MODE_MULTI)
        game.save_game(ACT_SAVE)
        self.assertTrue(game.saved)
        game.saved = True
        game.save_game(ACT_STOP)
        self.assertTrue(game.end_game)
        game.saved = False
        game.save_game(ACT_STOP)
        