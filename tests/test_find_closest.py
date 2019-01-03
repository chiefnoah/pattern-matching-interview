from unittest import TestCase
import random
import logging
from find_closest_num import find_closest

logging.basicConfig(level=logging.INFO)

class FindClosesTestCase(TestCase):

    def test_bulk(self):
        test_cases = [
            # list, target, expected
            ([1, 2, 3, 4, 5, 6], 3, 3),
            ([1, 2, 4, 5, 6, 7], 3, 2),
            ([1, 2], 3, 2),
            ([1, 2], 2, 2),
            ([1, 2], 1, 1),
            ([1, 2, 3, 5, 6, 7], 4, 3),
            ([1, 4, 18, 100], 50, 18),
            ([1, 2, 3], 4, 3),
            ([1, 2, 3], 3, 3)
        ]
        for case in test_cases:
            with self.subTest(target=case[1], expected=case[2]):
                result = find_closest(case[0], case[1])
                logging.info("expected: {} == result: {}".format(case[2], result))
                self.assertEqual(result, case[2])

    def test_big(self):
        l = []
        for x in range(1000000):
            l.append(x)

        target = random.randint(1, 1000000)
        l.remove(target)
        expected = target - 1


        result = find_closest(l, target)
        logging.info("expected: {} == result: {}".format(expected, result))
        self.assertEqual(expected, result)
