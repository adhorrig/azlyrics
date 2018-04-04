import unittest
from azlyrics import artists, songs, lyrics


class AzlyricsTests(unittest.TestCase):

    def test_artists(self):
        a = artists("T")
        self.assertIsNotNone(a)
        self.assertIn('Taylor Swift', a)

    def test_songs(self):
        s = songs("Taylor Swift")
        self.assertIsNotNone(s)
        self.assertIn('1989', s)

    def test_lyrics(self):
        wd = lyrics("Oasis", "Magic Pie")
        self.assertIsNotNone(wd)
