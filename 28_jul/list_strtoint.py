from operator import itemgetter

dictrandom = {"8":"hello","7":"hey","5":"shutup","52":"happy","43":"never mind","21":"okie bye","16":"thank you"}
list1 = list(dictrandom.keys())

results = list(map(int, list1))
print (sorted(results))
#print(itemgetter(2))
# listrandkeys = sorted(list(map(itemgetter(key) in dictrandom.items(),dictrandom)))
#listrandkeys = dict_random.sorted(key=itemgetter(1))
#print(listrandkeys)
#listrandkeys.sort()
#intkeys = int(dict_random,key=itemgetter(key)) 
#print(listrandkeys)
# sortedkeys = int(sortedkeys)
#print(intkeys)
#print(sortedkeys)


# print(listrandkeys)