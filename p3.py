# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
prime_list = []
num = int(raw_input("number for prime factorization:"))


def prime_factor(x):
    divisor = 2
    while divisor <= x:
        if x % divisor == 0:
            prime_list.append(divisor)
            x = x / divisor
        divisor += 1

    return prime_list

print prime_factor(num)
