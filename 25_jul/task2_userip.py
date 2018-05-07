#######################################
from sys import argv
def sum():
	print("Enter 3 nos. : ")
	script, a,b,c = argv
	#a = int(a); b = int(b); c = int(c)
	addition = int(a)+int(b)+int(c)
	return "Sum of {0} {1} {2} is ".format(a,b,c)+str(addition)
sumresult = sum()
print (sumresult)


#######################################
from math import sqrt
def sqrtofnum():
	num = float(input("Enter a num for sqrt:"))	#since result of input call is a string, we need to convert it to float inorder to perform math function
	return ("Sqrt of given num: " +str(sqrt(num)))
sqrtresult = sqrtofnum()	
print(sqrtresult)

