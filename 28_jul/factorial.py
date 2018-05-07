try:
	while True:
		num = int(input("Enter a num"))
		ans=1
		while num:
			ans = ans*num
			num -= 1
		print("Factorial of given no. is "+str(ans))
except KeyboardInterrupt:
	print("\nDone")