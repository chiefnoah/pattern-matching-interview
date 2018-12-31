from unittest import TestCase
import random
from find_closest import find_closest

class FindClosesTestCase(TestCase):


    def setUp(self):
        self.test_cases = [
            ([1, 2, 3, 4, 5, 6], 3, 3),
            ([1, 2, 4, 5, 6, 7], 3, 2),
            ([1, 2], 3, 2),
            ([1, 2], 2, 2),
            ([1, 2], 1, 1),
            ([1, 2, 3, 5, 6, 7], 4, 3),
        ]

    def test_bulk(self):
        for case in self.test_cases:
            result = find_closest(case[0], case[1])
            self.assertEqual(result, case[2])

    def test_big(self):
        l = []
        for x in range(1000000):
            l.append(x)

        target = random.randint(1, 1000000)
        l.remove(target)
        expected = target - 1


        result = find_closest(l, target)
        try:
            self.assertEqual(expected, result)
        except AssertionError:
            i = target in sl
            import ipdb;ipdb.set_trace()
