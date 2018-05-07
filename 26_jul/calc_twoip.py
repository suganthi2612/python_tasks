def plus(a,b):
	c = a+b
	return "Sum of {} and {} is ".format(a,b)+str(c)

def minus(a,b):
	c = a-b
	return "Diff btwn {} and {} is ".format(a,b)+str(c)

def mul(a,b):
	c = a*b
	return "Product of {} and {} is ".format(a,b)+str(c)

def div(a,b):
	c = a/b
	return "Share is "+str(c)

ch = str(input("Give your choice 1.{add} 2.{sub} 3.{mul} 4.{div}".format(add="Addition",sub="Subtraction",mul="Multiplication",div="Division")))

a = int(input("Enter a value for 'a' : "))
b = int(input("Enter a value for 'b' : "))

if(ch=="1" or ch=="Addition" or ch=="Add"):
	sumof = plus(a,b)
	print(sumof)

elif(ch=="2" or ch=="Subtraction" or ch=="Sub"):
	subof = minus(a,b)
	print(subof)

elif(ch=="3" or ch=="Multiplication" or ch=="Multiply"):
	mulof = mul(a,b)
	print(mulof)

elif(ch=="4" or ch=="Division" or ch=="Div"):
	divof = div(a,b)
	print(divof)

elif(ch==""):
	pass

else:
	print("\n Select appropriate option")

