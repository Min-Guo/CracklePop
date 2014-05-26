# Code CracklePop
# Min Guo
# May 22, 2014
# Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle instead of the number. If it is divisible by 5, print Pop. if it is divisible by both 3 and 5, print CracklePop.


def cracklePopOneHundred():
	for num in range(1, 101):
		print cracklePop(num)

def cracklePop(num):
	if (num % 3 == 0) and (num % 5 == 0):
		return "CracklePop"
	elif num % 3 == 0:
		return "Crackle"
	elif num % 5 == 0:
		return "Pop"
	else:
		return num

cracklePopOneHundred()


