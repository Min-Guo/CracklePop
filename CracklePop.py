# Code CracklePop
# Min Guo
# May 22, 2014
# Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle instead of the number. If it is divisible by 5, print Pop. if it is divisible by both 3 and 5, print CracklePop.

def CracklePop():

	for num in range(1, 101):
 		if (num % 3 == 0) and (num % 5 == 0):
 			print "CracklePop"
 		elif num % 3 == 0:
 			print "Crackle"
 		elif num % 5 == 0:
 			print "Pop"
 		else:
 			print num

CracklePop()