#######################################

def summation():
	total = int(input("How many nos. you wanna add "))
	nos = input("Enter " +str(total)+ " nos. with space seperated ")
	num = [int(x) for x in nos.split()]
	if(len(num) == total):
		sumres = sum(num)
		return sumres
	else:
		return "Not possible"
	#num = map(int,num)
	# sumres = sum(num)
	# return sumres
	#num = []
	#ip_list = input("Enter 3 nos. : ").split(" ")
	#for value in enumerate(ip_list):
	#	num = value
	#print(num)
sumresult = summation()
print (sumresult)

