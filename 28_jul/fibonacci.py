try:
	while True:
		num = int(input("Enter a num for fibonacci series"))
		i=0
		ans=0
		a=1
		b=0
		while(i<num):
			print (ans)
			b = ans+a
			ans=a
			a=b
			i += 1
except KeyboardInterrupt:
	print("Done")