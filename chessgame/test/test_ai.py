# pylint: disable=C

import unittest
import chessgame.main.consts as consts
from chessgame.main.game import Game


class AITest(unittest.TestCase):
    
    def test_ai_moves(self):
        game = Game("test")
        game.start_game("test")
        confdict = {'1::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '2::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '3::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '4::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '5::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '6::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '7::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0},
                    '8::7' : {consts.MV_FWD2 : (100/5), consts.MV_FWD1 : (100/6), consts.MV_LEFT : 0, consts.MV_RIGHT : 0}}
        self.assertEqual(game.ai_moves(),confdict)