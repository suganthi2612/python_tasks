def numip():
	try:
		total = int(input("How many nos. do you want to give "))
		nos = input("Enter " +str(total)+ " nos. with space seperated ")
		num = [int(x) for x in nos.split()]
		# print(num)
		# result = []
		if(len(num) == total):
			#result = [bool(s) for s in num if s%2==0]
			for element in num:
				if(element%2==0):
					print(str(element) +" is even")
				else:
					print(str(element)+" is odd")
		else:
			print("Not possible") 
		return ""
	except ValueError:
		return "Please enter int only"

try:
	while True:
		divtwo = numip()
		print(divtwo)
except KeyboardInterrupt:
	print("\nYou have Interrupted!!")
