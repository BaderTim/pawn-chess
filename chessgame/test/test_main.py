#pylint: disable=C

import unittest
import main
import sys
import chessgame.test.test_game_std as std

class MainTest(unittest.TestCase):

    def test_nav_back(self):
        std.stub_stdin(self,"l\nb\nx\nx")
        std.stub_stdouts(self)
        main.main()
        output = sys.stdout.getvalue()
        self.assertIn("Öffne Hauptmenü...", output)
    
    def test_nav_quit_main(self):
        std.stub_stdin(self,"x")
        std.stub_stdouts(self)
        self.assertEqual(main.main(), 1)

    def test_nav_quit_new(self):
        std.stub_stdin(self,"n\nx\nx")
        std.stub_stdouts(self)
        self.assertEqual(main.main(), 0)
    
    def test_nav_new(self):
        std.stub_stdin(self,"n\nm\nx\nx\nx")
        std.stub_stdouts(self)
        main.main()
        output = sys.stdout.getvalue()
        self.assertIn("Öffne Hauptmenü...", output)
    
    def test_mode_invalid(self):
        std.stub_stdin(self,"n\nfoo_bar\nx")
        std.stub_stdouts(self)
        main.main()
        output = sys.stdout.getvalue()
        self.assertIn("Fehler: 'foo_bar' konnte nicht zugeordnet werden. Bitte versuche es erneut.", output)
