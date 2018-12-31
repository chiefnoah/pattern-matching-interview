from unittest import TestCase
from pattern_matching import isMatch, lazyIsMatch
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
            #("", "*", True), # This doesn't work with the python regex parser, is it valid?
            ("asdfasf", "", False),
            ("", "a*", True),
            ("", "a*b*c*", True),
            ("b", "a*c*", False),
            ("aaaaabbbba", "a*ab*a", True),
            ("", "", True),
            ("aaaaaa", "*", False),
            # ("abaac", "aba*********c", True) # Doesn't work with the python regex parser? 
        ]

        self.false_failures = [
            ("aaaaaaaa", "aa*a", False),
            ("aaaaaa", "?a*a", False),
        ]

    def test_bulk(self):
        for test_case in self.test_cases:
            with self.subTest(text=test_case[0], pattern=test_case[1]):
                match = isMatch(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s", # info because by default it won't log debug or info
                                test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])

        for bad_case in self.false_failures:
            with self.subTest(msg="BAD", text=test_case[0], pattern=test_case[1]):
                match = isMatch(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s",  # info because by default it won't log debug or info
                                test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])

    def test_lazy_bulk(self):
        for test_case in self.test_cases:
            with self.subTest(msg="LAZY", text=test_case[0], pattern=test_case[1]):
                match = lazyIsMatch(test_case[0], test_case[1])
                logging.info("%s match %s = %s should be %s",
                        test_case[0], test_case[1], match, test_case[2])
                self.assertEqual(match, test_case[2])
