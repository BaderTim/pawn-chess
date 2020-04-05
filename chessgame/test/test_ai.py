# pylint: disable=C

import unittest
import chessgame.main.consts as consts
import chessgame.test.test_game_std as std
from chessgame.main.game import Game
from chessgame.main.pawn import Pawn


class AITest(unittest.TestCase):
    
    def test_ai_moves(self):
        std.stub_stdouts(self)
        game = Game(consts.MODE_TEST)
        game.start_game(consts.MODE_TEST)
        confdict = {'1::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '2::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '3::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '4::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '5::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '6::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '7::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '8::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0}}
        self.assertEqual(game.ai_moves(),confdict)
        game.figures = [Pawn(4,6,consts.COLOR_BLACK),Pawn(3,5,consts.COLOR_WHITE),Pawn(4,5,consts.COLOR_WHITE),Pawn(5,5,consts.COLOR_WHITE)]
        confdict = {'4::6':{consts.MV_FWD2 : 0, consts.MV_FWD1 : 0, consts.MV_LEFT : (100/5)+20, consts.MV_RIGHT : (100/5)+20}}
        self.assertEqual(game.ai_moves(),confdict)

    def test_get_best_move(self):
        std.stub_stdouts(self)
        game = Game(consts.MODE_TEST)
        testdict = ("2::6", {consts.MV_FWD2 : 0, consts.MV_FWD1 : (100/5), consts.MV_LEFT: (100/5) + 20, consts.MV_RIGHT: 0})
        retval = ["2::6" , consts.MV_LEFT, (100/5) + 20]
        self.assertEqual(game.get_best_move(testdict), retval)
    
    def test_ai_decide(self):
        std.stub_stdouts(self)
        game = Game(consts.MODE_TEST)
        testlist = [['2::7', 'm2', (100/5)], ['4::5', 'r', (100/4) +20], ['6::2', 'm', 100]]
        self.assertEqual(game.ai_decide(testlist),['6::2','m',100])
        testlist = [['2::7', 'm2', (100/5)], ['4::5', 'r', (100/4) +20], ['6::2', 'm', 100], ['5::2', 'm', 100]]
        self.assertIn(game.ai_decide(testlist), (['6::2', 'm', 100], ['5::2', 'm', 100]))