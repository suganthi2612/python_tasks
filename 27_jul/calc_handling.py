import sys
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
	try:
		c = a/b
		return "Share is "+str(c)
	except ZeroDivisionError:
		return "Value of divisor cannot be 0."

try:
	while True:
		ch = input("Give your choice 1.{add} 2.{sub} 3.{mul} 4.{div} :".format(add="Addition",sub="Subtraction",mul="Multiplication",div="Division"))
		try:
			ch = int(ch)
			if(1<=ch<=4):
				a = int(input("Enter a value for 'a' : "))
				b = int(input("Enter a value for 'b' : "))
				if(ch==1):
					sumof = plus(a,b)
					print(sumof)

				elif(ch==2):
					subof = minus(a,b)
					print(subof)

				elif(ch==3):
					mulof = mul(a,b)
					print(mulof)

				else:
					divof = div(a,b)
					print(divof)

			else:
				print("Invalid option. Select from 1-4 only.")
			# except (ValueError,TypeError):
			# print("Only integers are accepted.")
		except ValueError:
			print("Only integers are accepted.")
except KeyboardInterrupt:
	#pass
	print("\nYou have Interrupted!!")
