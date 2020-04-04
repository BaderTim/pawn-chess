# pylint: disable=C
import unittest
from chessgame.main.game import Game
from chessgame.main.consts import COLOR_BLACK
from chessgame.main.consts import COLOR_WHITE
from chessgame.main.consts import PLAYER_BLACK
from chessgame.main.consts import PLAYER_WHITE
from chessgame.main.pawn import Pawn


class GameTest(unittest.TestCase):
    '''
        Testclass for Game
    '''

    def test_get_figure_machine_input(self):
        game = Game("test")
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            machine_input = f"{counter + 1}::2"
            self.assertEqual(game.get_figure(machine_input).get_pos_x(), Pawn(counter + 1, 2, COLOR_WHITE).get_pos_x())
            self.assertEqual(game.get_figure(machine_input).get_pos_y(), Pawn(counter + 1, 2, COLOR_WHITE).get_pos_y())
            self.assertEqual(game.get_figure(machine_input).get_color(), Pawn(counter + 1, 2, COLOR_WHITE).get_color())
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
            machine_input = f"{counter + 1}::7"
            self.assertEqual(game.get_figure(machine_input).get_pos_x(), Pawn(counter + 1, 7, COLOR_BLACK).get_pos_x())
            self.assertEqual(game.get_figure(machine_input).get_pos_y(), Pawn(counter + 1, 7, COLOR_BLACK).get_pos_y())
            self.assertEqual(game.get_figure(machine_input).get_color(), Pawn(counter + 1, 2, COLOR_BLACK).get_color())

    def test_get_figure_user_input(self):
        game = Game("test")
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            user_input = f"{str(chr(counter+65))}2"
            self.assertEqual(game.get_figure(user_input).get_pos_x(), Pawn(counter + 1, 2, COLOR_WHITE).get_pos_x())
            self.assertEqual(game.get_figure(user_input).get_pos_y(), Pawn(counter + 1, 2, COLOR_WHITE).get_pos_y())
            self.assertEqual(game.get_figure(user_input).get_color(), Pawn(counter + 1, 2, COLOR_WHITE).get_color())
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
            user_input = f"{str(chr(counter+65))}7"
            self.assertEqual(game.get_figure(user_input).get_pos_x(), Pawn(counter + 1, 7, COLOR_BLACK).get_pos_x())
            self.assertEqual(game.get_figure(user_input).get_pos_y(), Pawn(counter + 1, 7, COLOR_BLACK).get_pos_y())
            self.assertEqual(game.get_figure(user_input).get_color(), Pawn(counter + 1, 2, COLOR_BLACK).get_color())

    def test_check_for_hit_none(self):
        game = Game("test")
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
        fig_counter_pre = len(game.figures)
        game.check_for_hit(5, 5, PLAYER_BLACK)
        fig_counter_pos = len(game.figures)
        self.assertEqual(fig_counter_pre, fig_counter_pos)

    def test_check_for_hit_true(self):
        game = Game("test")
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
        fig_counter_pre = len(game.figures)
        game.check_for_hit(1, 2, PLAYER_BLACK)
        fig_counter_pos = len(game.figures)
        self.assertNotEqual(fig_counter_pre, fig_counter_pos)

        fig_counter_pre = fig_counter_pos
        game.check_for_hit(1, 7, PLAYER_WHITE)
        fig_counter_pos = len(game.figures)
        self.assertNotEqual(fig_counter_pre, fig_counter_pos)

    def test_check_for_hit_false(self):
        game = Game("test")
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
        fig_counter_pre = len(game.figures)
        game.check_for_hit(1, 2, PLAYER_WHITE)
        fig_counter_pos = len(game.figures)
        self.assertEqual(fig_counter_pre, fig_counter_pos)

        fig_counter_pre = fig_counter_pos
        game.check_for_hit(1, 7, PLAYER_BLACK)
        fig_counter_pos = len(game.figures)
        self.assertEqual(fig_counter_pre, fig_counter_pos)
