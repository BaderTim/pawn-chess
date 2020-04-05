#pylint: disable=C
import unittest
import chessgame.test.test_game_std as std
import sys
import os
from chessgame.main.save import Save
from chessgame.main.consts import COLOR_BLACK, COLOR_WHITE, MODE_TEST, ACT_LOAD
from chessgame.main.pawn import Pawn
from chessgame.main.game import Game


class SaveTest(unittest.TestCase):

    def test_save_game(self):
        std.stub_stdouts(self)
        std.stub_stdin(self, "test_file")
        game = Game(MODE_TEST)
        game.start_game(MODE_TEST)
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
        
        std.stub_stdouts(self)
        std.stub_stdin(self, "test_file")
        game = Game(ACT_LOAD)
        for idx, figure in enumerate(testlist, 0):
            self.assertEqual(game.figures[idx].to_string(), figure.to_string())
        self.assertEqual(game.game_mode, test_game_mode)

    def test_file_not_found(self):
        std.stub_stdouts(self)
        game = Game(MODE_TEST)
        save = Save(game, "nghrehugjlhgyduilgfvrawu7eztr5wsdfb")
        save.load_game()
        output = sys.stdout.getvalue()
        self.assertIn("Fehler: konnte 'nghrehugjlhgyduilgfvrawu7eztr5wsdfb.txt' nicht finden.",output)
    
    def test_load_falsified_mode(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\saved_files\\"
        std.stub_stdouts(self)
        file = open(path + "test_falsify_mode.txt", "w+")
        file.write("lol\nw_2#2\nb_4#7")
        file.close()
        
        game = Game(MODE_TEST)
        save = Save(game, 'test_falsify_mode.txt')
        save.load_game()
        output = sys.stdout.getvalue()
        self.assertIn("Fehler: Datei 'test_falsify_mode.txt' scheint einen fehlerhaften Spielmodi in Zeile 1 zu haben.",output)
    
    def test_load_falsify_color(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\saved_files\\"
        std.stub_stdouts(self)
        file = open(path + "test_falsify_color.txt", "w+")
        file.write(MODE_TEST + "\ng_2#2\nb_4#7")
        file.close()
        
        game = Game(MODE_TEST)
        save = Save(game, 'test_falsify_color.txt')
        save.load_game()
        output = sys.stdout.getvalue()
        self.assertIn("Fehler: Datei 'test_falsify_color.txt' scheint fehlerhafte Farben in Zeile 2 zu haben.",output)

    def test_load_falsified_coords_nums(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\saved_files\\"
        std.stub_stdouts(self)
        file = open(path + "test_falsify_coords.txt", "w+")
        file.write(MODE_TEST + "\nw_9#0\nb_4#7")
        file.close()
        
        game = Game(MODE_TEST)
        save = Save(game, 'test_falsify_coords.txt')
        save.load_game()
        output = sys.stdout.getvalue()
        self.assertIn("Fehler: Datei 'test_falsify_coords.txt' scheint fehlerhafte Koordinaten in Zeile 2 zu haben.",output)

    def test_load_falsified_coords_text(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\saved_files\\"
        std.stub_stdouts(self)
        file = open(path + "test_falsify_coords_2.txt", "w+")
        file.write(MODE_TEST + "\nw_f#e\nb_4#7")
        file.close()

        game = Game(MODE_TEST)
        save = Save(game, 'test_falsify_coords_2.txt')
        save.load_game()
        output = sys.stdout.getvalue()
        self.assertIn("Fehler: Datei 'test_falsify_coords_2.txt' scheint fehlerhafte Koordinaten zu haben.",output)



