dict_random = {"8":"hello","7":"hey","5":"shutup","52":"happy","43":"never mind","21":"okie bye","16":"thank you"}

dict_random1 = {8:"hello",7:"hey",5:"shutup",52:"happy",43:"never mind",21:"okie bye",16:"thank you"}

# print(dict_random)
# print(type(dict_random))
#	list_sort = sorted(dict_random)
#	print(list_sort)
#print(dict_random.items())
#dict_item=dict_random.items()
#	print(dict_random.keys())
# keys = dict_random.keys()
# print(keys)
list_key=list()
for (key,value) in dict_random.items():
	list_key.append(key)
print("List of first set of keys(keys with quotes) : " +str(list_key)) 
#print(type(list_key))
print("Sorted list of first set of keys : "+str(sorted(list_key)))


list_key1=list()
for (key,value) in dict_random1.items():
	list_key1.append(key)
print("List of second set of keys(keys without quotes) : " +str(list_key1))
#print(type(list_key))
print("Sorted list of second set of keys : "+str(sorted(list_key1)))