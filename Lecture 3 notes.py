#Lecture 3 notes


#Gives perfect square without check
# x = 16
# ans = 0
# while ans*ans < x:
# 	ans = ans + 1
# print ans

#gives square root but checks if it is a perfect square and checks for negativity and prints each step
# x = 16
# ans = 0
# if x >= 0:
# 	while ans*ans < x:
# 		ans = ans + 1
# 	if ans*ans != x:
# 		print x,'is not a perfect square'
# 	else: print ans
# else: print x, 'is a negative number'

#Finds all the divisors of a number
# x = 10
# i = 1
# while i<x:
# 	if x%i == 0:
# 		print 'divisor', i
# 	i= i+1

#Finds all the divisors of a number using range
# x = 10
# for i in range(1,x):
#         if x%i == 0:
#             print 'divisor ',i

#Finds all the divisors of a number and puts them in a tuple
x = 100
divisors = ()
for i in range (1,x):
    if x%i == 0:
        divisors = divisors + (i,)
print divisors [0:]
