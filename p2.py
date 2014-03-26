import unittest


def solution_one(limit):
    def gen(max):
        a, b = 1, 2
        while a < max:
            yield a
            a, b = b, a + b

    result = 0
    for n in gen(limit):
        if n % 2 == 0:
            result += n
    return result


class TestSolutions(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution_one(144), 44)

if __name__ == '__main__':
    unittest.main()
