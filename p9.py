def getTriplet():
    #check if a^2 + b^2 = (bound - a - b)^2
    a = 3
    bound = 1000
    for x in range (a, (bound - 3) / 3):
        for y in range((a + 1), (bound - a)):
            print x, y 
    
getTriplet()

# import math 

# a = 1
# b = a + 1
# c = b + 1

# total = a + b + c

# while total < 1001:
#     while total < 1001:
#         #print "a " + str(a)+ " b " + str(b) + " c " + str(c)
#         b += 1
#         c = b + 1
#         total = a + b +c

#         while total < 1001:
#             if a + b + c == 1000:
#                 print "YES"
# 	            square = math.sqrt(sum)
# 	            if square.is_integer():
# 	                if square == c:
# 	                    print "a " + str(a)+ " b " + str(b) + " c " + str(c) 
# 	                    print "sum is"
# 	                    print sum
# 	                    print square
# 	                    print c
# 	                    print "is integer and square"
# 	                    print a * b * c
#             c += 1
#             total = a + b +c
			 
#     #print "a " + str(a)+ " b " + str(b) + " c " + str(c)    
#     a += 1
#     b = a + 1
#     c = b + 1
#     total = a + b +c
    
