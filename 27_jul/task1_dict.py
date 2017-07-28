dict1 = {"hello":1,"hey":2,"content":{"how are you":"fine","never give up":"okay"}}
print("Dict1 :\t"+str(dict1))
print("\nDict1 under \"content\" key :\t"+str(dict1["content"]))
print("\nDict1 keys :\t"+str(dict1.keys()))
dict2 = {"num":123,"text":"chat","pics":"insta","videos":"youtube","means":{"whatsapp":"add or block","insta":"block or unblock","quora":"ques or ans"}}
#print(dict2)
print("\nDict2 under \"means\" kwy :\t"+str(dict2["means"]))
print("\n Dict2 values : \t"+str(dict2.values()))
print("\n Quora value : \t"+str(dict2["means"]["quora"]))
