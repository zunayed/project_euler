import unittest


# def get_factors(number):
#     return [x for x in range(1, number + 1) if number % x == 0]

def get_factors(n):

    return list(set(reduce(list.__add__,
              ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def get_trangle_num(n):
    # return sum(range(n + 1))
    return n * (n + 1) / 2


def get_tri_500_factors():
    found = False
    x = 1
    while not found:
    # for x in range(0, 20):
        # print len(get_factors(get_trangle_num(x)))

        if len(get_factors(get_trangle_num(x))) > 500:
            found = True
            print len(get_factors(get_trangle_num(x)))
            return x

        x += 1


class TestSolutions(unittest.TestCase):

    def test_get_factors(self):
        self.assertEqual(get_factors(1), [1])
        self.assertEqual(get_factors(3), [1, 3])
        self.assertEqual(get_factors(28), [1, 2, 4, 7, 14, 28])

    def test_solution_two(self):
        self.assertEqual(get_trangle_num(7), 28)

    def test_problem_solution(self):
        pass
        # self.assertEqual(get_tri_500_factors(), 7)


print get_tri_500_factors()


# if __name__ == '__main__':
#     unittest.main()
