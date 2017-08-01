try:
	while True:
		strip = input("Pls enter a string :")

		if (strip.isalpha()):
			print("It is a string")
			strchar = [letter for letter in strip]
			# for letter in strip:
			# 	strchar.append(letter)
			print(strchar)
			strlen = len(strip)
			print(strlen)
			initlen=0
			# if(initlen<strlen):
			# 	if(strip[initlen] == strip[strlen-1]):
			# 		initlen += 1
			# 		strlen -= 1
			# 		print()
			# 	print("Given string is a palindrome")
			# else:
			# 	print("Given string is not a palindrome")
			if(strip == strip[::-1]):
				print("It is palindrome")
			else:
				print("Not a palindrome")
		else:
			print("Enter char. alone")
except KeyboardInterrupt:
	print("Interrupted!!")


