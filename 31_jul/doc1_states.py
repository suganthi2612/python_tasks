#create a mapping of state to abbreviation
states={
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}	#declaring a dictionary of states with states and abbrev as key and value resp

#create a baisc set of states and some cities in them
cities={
	'CA':'San Francisco',
	'MI':'Detriot',
	'FL':'Jacksonville'
}	#declaring a dictionary of cities with the abbrev and corres. cities as key and value 

#add some more cities
cities['NY']='New York'	#adding new pair to dict cities
cities['OR']='Portland'

#print out some cities
print '-' * 10		# printing - for 10 times in same line
print "NY State has: ", cities['NY']	# printing the value of 'NY' from dict cities 
print "OR State has: ", cities['OR']	# printing the value of 'OR' from dict cities

#print out some states
print '-' * 10		# printing - for 10 times in same line
print "Michigan has: ", states['Michigan']	# printing the value of 'Micigan' from dict states
print "Florida has: ", states['Florida']	# printing the value of 'Florida' from dict states

#do it by using the state then cities dict
print '-' * 10		# printing - for 10 times in same line
print "Michigan has: ", cities[states['Michigan']]	# printing the value of 'MI' from dict cities, where 'MI' is value of states['Michigan']
print "Florida has: ", cities[states['Florida']]	# printing the value of 'FL' from dict cities, where 'FL' is value of states['Florida']

#print every state abbreviation
print '-' * 10		# printing - for 10 times in same line
for state,abbrev in states.items():					#getting keys and values from dict states
	print "%s is abbreviated %s" %(state,abbrev)	#printing states and abbrev from states dict using string formatting(placeholder)

#print every city in state
print '-' * 10		# printing - for 10 times in same line
for abbrev,city in cities.items():					#getting keys and values from dict cities
	print "%s has the city %s" %(abbrev,city)		#printing abbrev and corres. cities from dict cities

# now do both at the same time
print '-' * 10		# printing - for 10 times in same line
for state,abbrev in states.items():					#getting keys and values from dict states
	print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])	#printing the states and its abbrev from states dict, also with the values(cities) of abbrev from dict cities

print '-' * 10		# printing - for 10 times in same line
#safely get a abbreviation by state that might not be there
state = states.get('Texas',None)	#getting the value of key 'Texas' from dict states and returning "None" if that key is not available and storing them in a var 'state'

if not state:	#checking if var 'state' is not true 
	print "Sorry, no Texas."	

#get a city with a default value
city = cities.get('TX','Does not exist')	#same as above, with dict cities and returning "Does not exist" if 'TX' key is not there
print "The city for the state 'TX' is: %s" % city	#returning the value stored in var 'city'

def Map(num_buckets=256):		#defining a func "Map" with num_buckets as its arg
	"""Initiates a Map with the given number of buckets."""
	aMap = []		#initializing a var aMap
	for i in range(0,num_buckets):	
		aMap.append([])
	return aMap

def Map_hash(aMap,key):			#defining a func Map_hash with two var as args, aMap and key
	"""Given a key this create a number and then convert it to and 
index for the aMap's buckets."""
	return hash(key) %len(aMap)

def Map_get_bucket(aMap,key):	#defining a func Map_get_bucket with two var as args, aMap and key
	"""Given a key, find the bucket where it would go."""
	bucket_id = Map_hash(aMap,key)
	return aMap[bucket_id]

def Map_get_slot(aMap,key,default=None):	
	"""Returns the index, key, and value of a slot found in a 
bucket."""
	bucket = Map_get_bucket(aMap, key)
	for i,kv in enumerate(bucket):
		k,v = kv
		if key == k:
			return i, k, v
	return -1, key, default

def Map_get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = Map_get_slot(aMap, key, default=default)
	return v

def Map_set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = Map_get_bucket(aMap, key)
	i, k, v = Map_get_slot(aMap, key)

	if v:
		bucket[i] = (key,value)
	else:
		bucket.append((key,value))

def Map_delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = Map_get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v =  bucket[i]
		if key == k:
			del bucket[i]
			break

def Map_list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k,v in bucket:
				print k,v

# The tests that it will work.

jazz = Map()
Map_set(jazz, 'Miles Davis', 'Flamenco Sketches')
# confirms set will replace previous one
Map_set(jazz, 'Miles Davis', 'King of Blue')
Map_set(jazz, 'Duke Ellington', 'Beginning To See The Light')
Map_set(jazz, 'Bily Strayhorn', 'Lush Life')	

print "---- List Test ----"
Map_list(jazz)

print "---- Get Test ----"
print Map_get(jazz, 'Miles Davis')
print Map_get(jazz, 'Duke Ellington')
print Map_get(jazz, 'Billy Strayhorn')

print "---- Delete Test ----"
print "** Goodbye Miles"
Map_delete(jazz, "Miles Davis")
Map_list(jazz)

print "** Goodbye Duke"
Map_delete(jazz,"Duke Ellington")
Map_list(jazz)

print "** Goodbye Billy"
Map_delete(jazz, "Billy Strayhorn")
Map_list(jazz)

print "** Goodbye Pork Pie Hat"
Map_delete(jazz, "Charles Mingus")
