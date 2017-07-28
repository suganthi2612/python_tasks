dict1 = {"hello":1,"hey":2,"content":{"how are you":"fine","never give up":"okay"}}
dict2 = {"num":123,"text":"chat","pics":"insta","videos":"youtube","means":{"whatsapp":"add or block","insta":"block or unblock","quora":"ques or ans"}}

#dict3 = dict(dict1.items() + dict2.items())
dict3 = {}
for diction in [dict1,dict2]:
	dict3.update(diction)
print("Combined dict : \t"+str(dict3))
