########################
def example():
	print("hi")
	z= 9+11
	return z
z = example()
print(z)


########################
def add(n1,n2):
	sum = n1 + n2
	return sum
a = add(12,23)
print (a)


#########################
def nothing():
	pass
nothing()


x=6
def somefunc():
	print(x)
	x = x + 10
	print(x)
somefunc()