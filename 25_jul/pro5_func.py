def cube(num):
	cubenum = num**3
	return cubenum
cube(5)

newvar = cube(5)
print("newvar "+str(newvar))
#print(cube.cubenum) wont work since we try to access local variable