from sys import argv	#importing argv function from sys module, in order to get the user input

script, filename = argv	#assigning argv to the var "filename" and initializing script 

txt = open(filename)	#opening "filename" which should be a file from user and storing it in "txt"

print "Here's your file %r:" % filename	#printing the filename
print txt.read()	#reading the file stored in "txt" var

print "Type the filename again:"	#printing a line
file_again = raw_input("> ")	#getting another filename from user using raw_input() but this works with python2 and input() should work with python3, storing it in var "file_again"

txt_again = open(file_again)	#opening the latter file and storing in a var 

print txt_again.read()	#reading the file stored in txt_again
