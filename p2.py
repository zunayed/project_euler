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


def solution_two(limit):
    x = y = 1
    sum = 0
    while (sum < limit):
        sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum


class TestSolutions(unittest.TestCase):

    def test_solution_one(self):
        self.assertEqual(solution_one(144), 44)

    def test_solution_two(self):
        self.assertEqual(solution_two(144), 44)

if __name__ == '__main__':
    unittest.main()
