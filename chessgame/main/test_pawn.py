# pylint: disable=C
import unittest
from pawn import Pawn
from exceptions import OutOfBoundsException
from consts import GAME_SIZE
from consts import COLOR_BLACK
from consts import COLOR_WHITE


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
        f = Pawn(0, 0, COLOR_WHITE)
        self.assertFalse(f.move_to(0, 0, COLOR_BLACK))

        f = Pawn(1, 1, COLOR_WHITE)
        self.assertFalse(f.move_to(1, 1, COLOR_BLACK))
        self.assertFalse(f.move_to(1, 1, None))

        self.assertFalse(f.move_to(1, 2, None))
        self.assertFalse(f.move_to(0, 1, None))
        self.assertFalse(f.move_to(2, 1, None))

        self.assertFalse(f.move_to(1, 2, None))
        self.assertFalse(f.move_to(1, 2, COLOR_BLACK))

        self.assertFalse(f.move_to(1, 0, COLOR_BLACK))
        self.assertFalse(f.move_to(0, 0, None))
        self.assertFalse(f.move_to(2, 0, None))

        self.assertFalse(f.move_to(3, 0, COLOR_BLACK))
        self.assertFalse(f.move_to(3, 0, None))

        f = Pawn(2, 0, COLOR_WHITE)
        with self.assertRaises(OutOfBoundsException):
            self.assertFalse(f.move_to(2, -1, None))
        with self.assertRaises(OutOfBoundsException):
            self.assertFalse(f.move_to(1, -1, COLOR_BLACK))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertFalse(f.move_to(0, GAME_SIZE-3, COLOR_WHITE))

    def test_move_allowed_b(self):
        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(1, 2, None))
        self.assertTrue(f.get_position() == (1, 2))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(0, 2, COLOR_WHITE))
        self.assertTrue(f.get_position() == (0, 2))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(2, 2, COLOR_WHITE))
        self.assertTrue(f.get_position() == (2, 2))

    def test_move_allowed_w(self):
        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(1, GAME_SIZE-3, None))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-3))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(0, GAME_SIZE-3, COLOR_BLACK))
        self.assertTrue(f.get_position() == (0, GAME_SIZE-3))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(2, GAME_SIZE-3, COLOR_BLACK))
        self.assertTrue(f.get_position() == (2, GAME_SIZE-3))

    def test_move_double_at_start_b(self):
        f = Pawn(1, 1, COLOR_BLACK)
        self.assertTrue(f.move_to(1, 3, None))
        self.assertTrue(f.get_position() == (1, 3))

        f = Pawn(1, 1, COLOR_BLACK)
        self.assertFalse(f.move_to(1, 3, COLOR_WHITE))
        self.assertTrue(f.get_position() == (1, 1))

        f = Pawn(1, 2, COLOR_BLACK)
        self.assertFalse(f.move_to(1, 4, None))
        self.assertTrue(f.get_position() == (1, 2))

    def test_move_double_at_start_w(self):
        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertTrue(f.move_to(1, GAME_SIZE-4, None))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-4))

        f = Pawn(1, GAME_SIZE-2, COLOR_WHITE)
        self.assertFalse(f.move_to(1, GAME_SIZE-4, COLOR_BLACK))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-2))

        f = Pawn(1, GAME_SIZE-3, COLOR_WHITE)
        self.assertFalse(f.move_to(1, GAME_SIZE-5, None))
        self.assertTrue(f.get_position() == (1, GAME_SIZE-3))

if __name__ == "__main__":
    unittest.main()