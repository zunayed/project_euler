#2520 is the smallest number that can be divided by each
#of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible
#by all of the numbers from 1 to 20?
bool(1)
num_found = bool(0)
num = 1
while num_found == bool(0):
    for y in range(10, 20):
        if num % y == 0:
            num_found = bool(1)
        else:
            num_found = bool(0)
            break

    if num_found == bool(1):
            print num
    num = num + 1
    
print num
