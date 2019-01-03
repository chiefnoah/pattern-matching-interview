from unittest import TestCase, skip
from pattern_matching import isMatch, lazyIsMatch, isMatch2, isMatch3
import logging

logging.basicConfig(level=logging.DEBUG)

class MatcherTestCase(TestCase):

    def setUp(self):

        self.test_cases = [
            # string (s), pattern (p), match?
            ("abaaaaba", "abaaaaba", True),
            ("b", "a*b", True),
            ("aaab", "a*b", True),
            ("ab", "a*b", True),
            ("abaaaba", "abaaabc", False),
            ("ababa", "ab?ba", True),
            ("ababa", "abc?ba", False),
            ("abbaaaaaabac", "abba*abac", True),
            ("abbaaaaacc", "ab*a*c*", True),
            ("aaaaaaaaaa", "a*", True),
            ("aaaaaaaab", "*b", False),
            ("aaaaaab", "a*", False),
            ("baaaaaa", "a*", False),
            ("bbb", "bba*b", True),
            ("ababaaaaabaacd", "ababa*ba?cd", True),
            ("aaaaaaaaaaaaaaaaaaa", "a*", True),
            ("aaaa", "?aaa", True),
            ("baaa", "?aaa", True),
            ("baaa", "a?a", False),
            # ("", "*", True), # This doesn't work with the python regex parser, is it valid?
            ("asdfasf", "", False),
            ("", "a*", True),
            ("", "a*b*c*", True),
            ("b", "a*c*", False),
            ("aaaaabbbba", "a*ab*a", True),
            ("", "", True),
            ("aaaaaa", "*", False),
            # ("abaac", "aba*********c", True), # Doesn't work with the python regex parser? 
            ("aaaaaaaa", "aa*a", True),
            ("aaaaaa", "?a*a", True),
            ("aaaaaaaa", "a*?a", True),
            ("acb", "a?b", True),
            ("ahb", "a?b", True),
            ("b", "a*b", True),
            ("aaab", "a*b", True),
            ("ab", "a*b", True),
            ("aaacde", "a*aaacde", True),
            ("aaabc", "?a*b?", True),
            ("aaabc", "a*?c", True), # <-- This was the hardest test to get passing
            ("aaaaaaab", "a*aa?ab", True),
            ("aaabc", "a*a?b?", True)
        ]
    @skip("Tests for old implementation")
    def test_bulk(self):
        for test_case in self.test_cases:
            with self.subTest(text=test_case[0], pattern=test_case[1]):
                match = isMatch(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s", 
                                test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])

    def test_lazy_bulk(self):
        for test_case in self.test_cases:
            with self.subTest(msg="LAZY", text=test_case[0], pattern=test_case[1]):
                match = lazyIsMatch(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s",
                        test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])

    @skip("Tests for old implementation")
    def test_bulk_v2(self):
        for test_case in self.test_cases:
            with self.subTest(text=test_case[0], pattern=test_case[1]):
                match = isMatch2(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s",
                             test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])

    @skip("Tests for old implementation")
    def test_bulk_bad_tests_v2(self):
        for test_case in self.false_negatives_v2:
            with self.subTest(text=test_case[0], pattern=test_case[1]):
                match = isMatch2(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s",  
                             test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])
                
    def test_bulk_v3(self):
        for test_case in self.test_cases:
            with self.subTest(text=test_case[0], pattern=test_case[1]):
                match = isMatch3(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s",  
                             test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])
