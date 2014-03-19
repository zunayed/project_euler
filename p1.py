'''
if we list all the natural numbers below 10 that
are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_of_multiples_under(number):
    multiples = []
    for number in xrange(0, number):
        if number % 5 == 0 or number % 3 == 0:
            multiples.append(number)

    return sum(multiples)

print sum_of_multiples_under(1000)
