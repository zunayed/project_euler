import operator
import functools

with open('resources/p11_input.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = [int(item) for item in data[i].split(' ')]



def scan_row(row):
    greatest_sum = 0
    for i in range(len(row)):
        if i + 3 < len(row):
            print "multiplying: ", row[i:i+4]
            current_sum = functools.reduce(operator.mul, row[i:i+4], 1)
            if current_sum > greatest_sum:
                greatest_sum = current_sum            

    return greatest_sum
