def divthree():
	try:
		n = int(input("Enter n nos "))
		num = input("Enter "+str(n)+" integers with space separated ")
		noips = [int(x) for x in num.split()]
		result = list()
		if(len(noips) == n):
			result = [bool(x) for x in noips if x%3==0]
			return result

			# for element in noips:
			# 	if(element%3==0):
			# 		return True
			# 	else:
			# 		return False
		else:
			return "Not possible. Enter specified no. of int"
	except ValueError:
		return "Please enter int only"

try:
	while True:
		result = divthree()
		print(result)
except KeyboardInterrupt:
	print("Interrupted!")
