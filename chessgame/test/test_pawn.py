# pylint: disable=C
import unittest
from chessgame.main.pawn import Pawn
from chessgame.main.consts import GAME_SIZE
from chessgame.main.consts import COLOR_BLACK
from chessgame.main.consts import COLOR_WHITE


class PawnTest(unittest.TestCase):

    def test_get_pos(self):
        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.get_position() == (1, 1))
        f = Pawn(2, 2, COLOR_WHITE)
        self.assertTrue(f.get_position() == (2, 2))
        f = Pawn(1, 2, COLOR_WHITE)
        self.assertTrue(f.get_position() == (1, 2))

    def test_move_not_allowed_b(self):
        f = Pawn(5, 5, COLOR_BLACK)
        self.assertEqual(f.move_to(5, 4, COLOR_WHITE), 0)

        f = Pawn(3, 3, COLOR_BLACK)
        self.assertEqual(f.move_to(3, 2, COLOR_WHITE), 0)
        self.assertEqual(f.move_to(4, 3, None), 0)

        self.assertEqual(f.move_to(1, 1, None), 0)
        self.assertEqual(f.move_to(1, 2, None), 0)
        self.assertEqual(f.move_to(2, 1, None), 0)

        self.assertEqual(f.move_to(2, 1, None), 0)
        self.assertEqual(f.move_to(2, 1, COLOR_WHITE), 0)

        self.assertEqual(f.move_to(1, 2, COLOR_BLACK), 0)
        self.assertEqual(f.move_to(3, 3, None), 0)
        self.assertEqual(f.move_to(2, 2, None), 0)

        self.assertEqual(f.move_to(4, 4, COLOR_WHITE), 0)
        self.assertEqual(f.move_to(4, 4, None), 0)

        f = Pawn(2, GAME_SIZE-1, COLOR_BLACK)
        self.assertEqual(f.move_to(2,GAME_SIZE, COLOR_BLACK), 0)
        self.assertEqual(f.move_to(3,GAME_SIZE-2, None), 0)

        f = Pawn(3, 3, COLOR_BLACK)
        self.assertEqual(f.move_to(3, 2, COLOR_BLACK), 0)

    def test_move_not_allowed_w(self):
        f = Pawn(2, 2, COLOR_WHITE)
        self.assertEqual(f.move_to(2, 2, COLOR_BLACK), 0)

        f = Pawn(2, 2, COLOR_WHITE)
        self.assertEqual(f.move_to(2, 2, COLOR_BLACK), 0)
        self.assertEqual(f.move_to(2, 2, None), 0)

        self.assertEqual(f.move_to(2, 6, None), 0)
        self.assertEqual(f.move_to(1, 2, None), 0)
        self.assertEqual(f.move_to(2, 1, None), 0)

        self.assertEqual(f.move_to(6, 2, None), 0)
        self.assertEqual(f.move_to(2, 3, COLOR_BLACK), 0)

        self.assertEqual(f.move_to(2, 1, COLOR_BLACK), 0)
        self.assertEqual(f.move_to(1, 1, None), 0)
        self.assertEqual(f.move_to(3, 1, None), 0)

        self.assertEqual(f.move_to(4, 1, COLOR_BLACK), 0)
        self.assertEqual(f.move_to(4, 1, None), 0)

        f = Pawn(3, 3, COLOR_WHITE)
        self.assertEqual(f.move_to(3, 2, None), 0)
        self.assertEqual(f.move_to(2, 0, COLOR_BLACK), 0)

        f = Pawn(2, GAME_SIZE-2, COLOR_WHITE)
        self.assertEqual(f.move_to(1, GAME_SIZE-3, COLOR_WHITE), 0)

    def test_move_allowed_b(self):
        f = Pawn(2, 5, COLOR_BLACK)
        self.assertEqual(f.move_to(2, 4, None), 1)
        f = Pawn(2, 4, COLOR_BLACK)
        self.assertEqual(f.move_to(3, 3, COLOR_WHITE), 1)
        f = Pawn(2, 3, COLOR_BLACK)
        self.assertEqual(f.move_to(1, 2, COLOR_WHITE), 1)

    def test_move_allowed_w(self):
        f = Pawn(3, 3, COLOR_WHITE)
        self.assertEqual(f.move_to(3, 4, None), 1)
        self.assertEqual(f.move_to(4, 4, COLOR_BLACK), 1)
        self.assertEqual(f.move_to(2, 4, COLOR_BLACK), 1)

    def test_get_methods(self):
        f = Pawn(4, 2, COLOR_WHITE)
        self.assertEqual(f.get_position(), (4, 2))
        self.assertEqual(f.get_pos_x(), 4)
        self.assertEqual(f.get_pos_y(), 2)
        self.assertEqual(f.get_color(), COLOR_WHITE)

        f = Pawn(4, 2, COLOR_BLACK)
        self.assertEqual(f.get_position(), (4, 2))
        self.assertEqual(f.get_pos_x(), 4)
        self.assertEqual(f.get_pos_y(), 2)
        self.assertEqual(f.get_color(), COLOR_BLACK)

        f = Pawn(7, 1, COLOR_WHITE)
        self.assertEqual(f.get_position(), (7, 1))
        self.assertEqual(f.get_pos_x(), 7)
        self.assertEqual(f.get_pos_y(), 1)
        self.assertEqual(f.get_color(), COLOR_WHITE)

        f = Pawn(7, 1, COLOR_BLACK)
        self.assertEqual(f.get_position(), (7, 1))
        self.assertEqual(f.get_pos_x(), 7)
        self.assertEqual(f.get_pos_y(), 1)
        self.assertEqual(f.get_color(), COLOR_BLACK)

        f = Pawn(2, 2, COLOR_WHITE)
        self.assertEqual(f.get_position(), (2, 2))
        self.assertEqual(f.get_pos_x(), 2)
        self.assertEqual(f.get_pos_y(), 2)
        self.assertEqual(f.get_color(), COLOR_WHITE)

        f = Pawn(2, 2, COLOR_BLACK)
        self.assertEqual(f.get_position(), (2, 2))
        self.assertEqual(f.get_pos_x(), 2)
        self.assertEqual(f.get_pos_y(), 2)
        self.assertEqual(f.get_color(), COLOR_BLACK)

        f = Pawn(6, 5, COLOR_WHITE)
        self.assertEqual(f.get_position(), (6, 5))
        self.assertEqual(f.get_pos_x(), 6)
        self.assertEqual(f.get_pos_y(), 5)
        self.assertEqual(f.get_color(), COLOR_WHITE)

        f = Pawn(6, 5, COLOR_BLACK)
        self.assertEqual(f.get_position(), (6, 5))
        self.assertEqual(f.get_pos_x(), 6)
        self.assertEqual(f.get_pos_y(), 5)
        self.assertEqual(f.get_color(), COLOR_BLACK)
