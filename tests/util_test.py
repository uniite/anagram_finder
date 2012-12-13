from StringIO import StringIO
import unittest

from modules.util import remove_punctuation, save_anagram_sets


class UtilTest(unittest.TestCase):

    def test_remove_punctuation(self):
        # Ensure the remove_punctuation unction removes everything but letters
        self.assertEqual("whatsthis", remove_punctuation("what's this?"))
        self.assertEqual("somestrangechars", remove_punctuation("some\nstrange\0chars"))
        # Ensure it doesn't change letter casing
        self.assertEqual("MixedCase", remove_punctuation("MixedCase"))

    def test_save_anagram_sets(self):
        # Ensure a list of lists is written out in the right format
        result = StringIO()
        save_anagram_sets([["foo", "bar"], ["tier", "tire"]], result)
        result.seek(0)
        self.assertEqual("foo,bar\ntier,tire\n", result.read())

