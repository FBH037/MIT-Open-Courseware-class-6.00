#pset1
#NEED TO DO: 






#7919 is the thousandth prime


oddintiger = 3
divisee = oddintiger - 2
numberprime = 1
#starting at one includes the prime number 2 which this script cant deal with

while (numberprime<1000):
	while (divisee > 1):
		if((oddintiger%(oddintiger - divisee))>0):
			divisee = divisee - 1 
#			print ('divisee'), divisee		
		else:
			oddintiger = oddintiger + 1
#			print 'New intiger', oddintiger
			divisee = oddintiger - 2

	pass
	print 'prime', oddintiger
	oddintiger = oddintiger + 1
#	print 'New intiger end', oddintiger
	divisee = oddintiger - 2
	numberprime = numberprime + 1


pass





# print 'prime', oddintiger
# 		oddintiger = oddintiger + 1		
# 		print 'New intiger', oddintiger
# 		numberprime = numberprime + 1
# 		print 'how many primes?', numberprime

# divisee = divisee - 1 
# 			print ('divisee'), divisee		



#print oddintiger
#print divisee
#print numberprime




# Problem2: sum of the log of all primes below a certain number

from math import *

oddintiger = 3
divisee = oddintiger - 2
numberprime = 1
sumlog = .301
#n is just the number to compute too
n = 100
#starting at one includes the prime number 2 which this script cant deal with
while (oddintiger<n):
	while (divisee > 1):
		if((oddintiger%(oddintiger - divisee))>0):
			divisee = divisee - 1 
#			print ('divisee'), divisee		
		else:
			oddintiger = oddintiger + 1
#			print 'New intiger', oddintiger
			divisee = oddintiger - 2

	pass
	sumlog = sumlog + (log(oddintiger))
	print 'sumlog', sumlog
	print 'prime', oddintiger
	oddintiger = oddintiger + 1
#	print 'New intiger end', oddintiger
	divisee = oddintiger - 2
	numberprime = numberprime + 1


pass
print 'ratio', (sumlog/oddintiger)










