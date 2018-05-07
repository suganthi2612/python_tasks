####################################

def helloworld():
	print("Hello World!")
helloworld()


####################################
def sumnums(a,b):
	c=a+b
	return c
d = sumnums(5,7)
print("Sum of given nos.: " +str(d))


####################################
from math import sqrt
def sqrtofnum(a):
	c = sqrt(a)
	return c
result = sqrtofnum(100)
print("Sqrt of 100 is: "+ str(result) )


####################################
import random
def randomnum():
	return ("Random integer between 1 and 10 : " +str(random.randint(1,10)) 
	+ "\n Random float between 1 and 8 : " +str(random.uniform(1,8))
	+ "\n Random float btwn [0.0 and 1.0) using built-in func random() : "+str(random.random()))
randresult = randomnum()
print (randresult)
