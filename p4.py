# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

ans = 0

for i in range(900, 1000):
        for x in range(900, 1000):
            result = i * x
            str_result = str(result)
            if str_result[0] == str_result[5] and str_result[1] == str_result[4] and str_result[2] == str_result[3]:
                num = int(str_result)
                if num > ans:
                    ans = num

print ans
            
    
