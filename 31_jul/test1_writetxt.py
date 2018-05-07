txtfile=open("sample.txt","w")
sometext="""Hey
How are you
What are you upto"""
txtfile.write(sometext)
txtfile=open("sample.txt","a")
txtfile.write(" sometext")
