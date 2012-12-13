from StringIO import StringIO
import unittest

from modules.anagram_finder import anagram_hash, extract_anagram_sets, find_anagrams


class AnagramFinderTest(unittest.TestCase):

    def test_anagram_hash(self):
        # Make sure the hashes only match for anagrams
        self.assertEqual(anagram_hash("abcd"), anagram_hash("dbca"))
        self.assertEqual(anagram_hash("brief"), anagram_hash("fiber"))
        # Not for words with a different amount of the same letter
        self.assertNotEqual(anagram_hash("abcd"), anagram_hash("dbbca"))
        # By default, punctuation should be ignored
        self.assertEqual(anagram_hash("abcd!"), anagram_hash("db ca"))
        # When specified, we consider punctuation
        self.assertNotEqual(anagram_hash("a'bcd", ignore_punc=False), anagram_hash("db'ca"))
        self.assertEqual(anagram_hash("a'bcd", ignore_punc=False), anagram_hash("db'ca", ignore_punc=False))
        # Case should be ignored as well
        self.assertEqual(anagram_hash("Abcd"), anagram_hash("dBca"))
        # There shouldn't be any length limit
        self.assertEqual(anagram_hash("abcd" * 1000), anagram_hash("dbca" * 1000))

    def test_extract_anagram_sets(self):
        words = ["brief", "tier", "tire", "fiber", "erit", "abc", "abcd", "ab", "cbda"]
        output = StringIO()
        # Ensure the anagrams are extracted, and sorted in the right order
        count = extract_anagram_sets(words, output)
        self.assertEqual(3, count)
        # What we expect, after being parsed into a list of lists
        expected_output = [["erit", "tier", "tire"], ["abcd", "cbda"], ["brief", "fiber"]]
        # Extract and parse the result from out StringIO object
        output.seek(0)
        output = [sorted(words.split(",")) for words in output.read().strip().split("\n")]
        # Ensure the output is as expected
        self.assertEqual(expected_output, output)

    def test_find_anagrams(self):
        words = ["brief", "tier", "tire", "fiber", "erit", "abc", "abcd", "ab", "cbda"]
        # Ensure find_anagrams processes our list of words correctly
        result = find_anagrams(words)
        # There should be three groups of anagrams
        self.assertEqual(3, len(result))
        # Check that all the groups are there, regardless of order
        result = sorted([sorted(group) for group in result])
        self.assertEqual([["abcd", "cbda"], ["brief", "fiber"], ["erit", "tier", "tire"]], result)
