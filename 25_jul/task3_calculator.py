############################
from sys import argv

a,b,c=4,3,2
def add():
	sum=a+b+c
	#val = 0
	#for i in range(3):
		#val += int(input())
	#return "Sum is"+str(val)
	return "Values added :"+str(sum)
#sumresult = add()
#print(sumresult)


def sub():
	subval = a-b-c
	return "Subtracted value: "+str(subval)
#subresult = sub()
#print(subresult)


def multiply():
	mul = a*b*c
	return "Product is: "+str(mul)
#mulresult = multiply()
#print(mulresult)


def division():
	div = a/b/c
	return "Sharing is: "+str(div)
#divresult = division()
#print(divresult)

plus="Addition"; minus="Subtraction"; prod="Multiplication"; share="Division"
userip = eval(input("Enter your choice 1.{} 2.{} 3.{} 4.{}".format(plus,minus,prod,share)))

if(userip==1):
	sumresult = add()
	print(sumresult)

elif(userip==2):
	subresult=sub()
	print(subresult)

elif(userip==3):
	mulresult=multiply()
	print(mulresult)

elif(userip==4):
	divresult=division()
	print(divresult)

else:
	print("Please enter appropriate choice")
