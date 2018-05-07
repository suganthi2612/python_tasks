
def add():
	val = 0
	for i in range(3):
		val += int(input())
	return "Sum is"+str(val)
	#return "Values added :"+str(sum)
sumresult = add()



plus="Addition"; minus="Subtraction"; prod="Multiplication"; share="Division"
userip = eval(input("Enter your choice 1.{} 2.{} 3.{} 4.{}".format(plus,minus,prod,share)))

if(userip==1):
	print(sumresult)

