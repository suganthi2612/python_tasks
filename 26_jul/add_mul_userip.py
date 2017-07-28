def plus():
	try:
		num = int(input("How many nos. do you want to add"))
		if(num==0):
			return "You cannot give 0."
		else:
			if(num==1):
				return "Requires atleast 2 nos. to add"
			else:
				print("Enter " +str(num)+ " nos.:")
				val = 0
				for i in range(num):
					#try:
						val += float(input())
					#except valueError:
					#	pass 
				return "Sum is " + str(val)
	except ValueError:
		print("Only integers are accepted.")


def mul():
	try:
		num = int(input("How many nos. do you want to multiply"))
		if(num==0):
			return "You cannot give 0."
		else:
			if(num==1):
				return "Requires atleast 2 nos. to multiply"
			else:
				print("Enter " +str(num)+ " nos.:")
				val = 1
				for i in range(num):
					val *= float(input())
				return "Product is " + str(val)
	except ValueError:
		print("Only integers are accepted.")


try:
	while True:
		ch = input("Select 1. Addition or 2. Multiplication ")
		try:
			ch = int(ch)
			if(ch==1):
				res = plus()
				print(res)
			elif(ch==2):
				res1 = mul()
				print(res1)
			else:
				print("Give 1 or 2")
		except ValueError:
			print("Only integers are accepted.")
except KeyboardInterrupt:
	print("\nYou have Interrupted!!")