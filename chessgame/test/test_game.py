# pylint: disable=C
import unittest
from chessgame.main.game import Game
from chessgame.main.consts import COLOR_BLACK
from chessgame.main.consts import COLOR_WHITE
from chessgame.main.consts import PLAYER_BLACK
from chessgame.main.consts import PLAYER_WHITE
from chessgame.main.consts import MODE_TEST
from chessgame.main.pawn import Pawn


class GameTest(unittest.TestCase):
    '''
        Testclass for Game
    '''

    def test_get_figure_machine_input(self):
        game = Game(MODE_TEST)
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
        game = Game(MODE_TEST)
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
        self.assertEqual(game.get_figure("A0"), None)
        self.assertEqual(game.get_figure("A9"), None)
        self.assertEqual(game.get_figure("K2"), None)

    def test_check_for_hit_none(self):
        game = Game(MODE_TEST)
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
        fig_counter_pre = len(game.figures)
        game.check_for_hit(5, 5, PLAYER_BLACK)
        fig_counter_pos = len(game.figures)
        self.assertEqual(fig_counter_pre, fig_counter_pos)

    def test_check_for_hit_true(self):
        game = Game(MODE_TEST)
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
        game = Game(MODE_TEST)
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

    def test_start_multiplayer_game_and_win(self):
        game = Game(MODE_TEST)
        game.figures = []
        game.win(PLAYER_WHITE)
        self.assertTrue(game.end_game)

        game = Game(MODE_TEST)
        game.figures = []
        game.win(PLAYER_WHITE)
        self.assertTrue(game.end_game)
        game.start_multiplayer_game()
        self.assertEqual(len(game.figures), 16)

    def test_start_ai_game(self):
        game = Game(MODE_TEST)
        game.figures = []
        game.win(PLAYER_WHITE)
        self.assertTrue(game.end_game)
        game.start_ai_game()
        self.assertEqual(len(game.figures), 16)

    def test_is_occupied(self):
        game = Game(MODE_TEST)
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
        self.assertEqual(game.is_occupied(1, 2), COLOR_WHITE)
        self.assertEqual(game.is_occupied(1, 7), COLOR_BLACK)
        self.assertEqual(game.is_occupied(5, 5), None)

    def test_update_ai_pawns(self):
        game = Game(MODE_TEST)
        game.figures = []
        for counter in range(8):
            game.figures.append(Pawn(counter + 1, 2, COLOR_WHITE))
            game.figures.append(Pawn(counter + 1, 7, COLOR_BLACK))
        game.update_ai_pawns()
        self.assertEqual(len(game.ai_pawns), 8)

    def test_toggle_player(self):
        game = Game(MODE_TEST)
        self.assertEqual(game.toggle_player(PLAYER_WHITE), PLAYER_BLACK)
        self.assertEqual(game.toggle_player(PLAYER_BLACK), PLAYER_WHITE)

    def test_make_move_invalid_input(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(1, 1, COLOR_BLACK)
        game.figures.append(f)

        self.assertEqual(game.make_move(f, PLAYER_WHITE, "test123", True), 3)

    def test_make_move_invalid_input_m2(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(3, 4, COLOR_WHITE)
        game.figures.append(f)
        f2 = Pawn(4, 3, COLOR_BLACK)
        game.figures.append(f2)

        self.assertEqual(game.make_move(f, PLAYER_WHITE, "m2", False), 4)
        self.assertEqual(game.make_move(f2, PLAYER_BLACK, "m2", False), 4)

    def test_make_move_valid_move(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(2, 2, COLOR_BLACK)
        game.figures.append(f)

        self.assertEqual(game.make_move(f, PLAYER_WHITE, "m2", False), 4)

    def test_make_move_invalid_move_m2(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(2, 2, COLOR_WHITE)
        game.figures.append(f)
        f2 = Pawn(2, 3, COLOR_BLACK)
        game.figures.append(f2)
        self.assertEqual(game.make_move(f, PLAYER_WHITE, "m2", True), 0)

        game.figures.clear()
        f = Pawn(2, 2, COLOR_WHITE)
        game.figures.append(f)
        f2 = Pawn(2, 3, COLOR_BLACK)
        game.figures.append(f2)	
        f3 = Pawn(2, 4, COLOR_WHITE)
        game.figures.append(f3)
        self.assertEqual(game.make_move(f, PLAYER_WHITE, "m2", True), 0)

    def test_make_move_invalid_move_m(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(2, 2, COLOR_WHITE)
        game.figures.append(f)
        f2 = Pawn(2, 3, COLOR_BLACK)
        game.figures.append(f2)
        self.assertEqual(game.make_move(f, PLAYER_WHITE, "m", True), 0)

    def test_make_move_invalid_move_diagonal(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(2, 2, COLOR_WHITE)
        game.figures.append(f)
        f2 = Pawn(3, 3, COLOR_WHITE)
        game.figures.append(f2)
        self.assertEqual(game.make_move(f, PLAYER_WHITE, "r", True), 0)
    
        game.figures.clear()
        f = Pawn(2, 2, COLOR_BLACK)
        game.figures.append(f)
        self.assertEqual(game.make_move(f, PLAYER_BLACK, "l", True), 0)

    def test_make_move_valid_move_m(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(2, 2, COLOR_WHITE)
        game.figures.append(f)
        f2 = Pawn(7, 7, COLOR_BLACK)
        game.figures.append(f2)
        self.assertEqual(game.make_move(f, PLAYER_WHITE, "m", True), 1)

    def test_make_move_valid_move_m_finish(self):
        game = Game(MODE_TEST)
        game.figures = []
        f = Pawn(4, 2, COLOR_BLACK)
        game.figures.append(f)
        self.assertEqual(game.make_move(f, PLAYER_BLACK, "m", True), 2)