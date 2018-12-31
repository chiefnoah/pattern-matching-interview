from unittest import TestCase
from pattern_matching import isMatch, lazyIsMatch
import logging


class MatcherTestCase(TestCase):

    def setUp(self):

        self.test_cases = [
            # string (s), pattern (p), match?
            ("abaaaaba", "abaaaaba", True),
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
            ("", "*", True),
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
            match = isMatch(test_case[0], test_case[1])
            logging.warning("%s match %s = %s should be %s", # warning because by default it won't log debug or info
                            test_case[0], test_case[1], match, test_case[2])
            self.assertEqual(match, test_case[2])

        for bad_case in self.false_failures:
            match = isMatch(test_case[0], test_case[1])
            logging.warning("%s match %s = %s should be %s",  # warning because by default it won't log debug or info
                            test_case[0], test_case[1], match, test_case[2])
            self.assertEqual(match, test_case[2])

    def test_lazy_bulk(self):
        for test_case in self.test_cases:
            match = lazyIsMatch(test_case[0], test_case[1])
        logging.warning("%s match %s = %s should be %s",
                        test_case[0], test_case[1], match, test_case[2])
        self.assertEqual(match, test_case[2])
