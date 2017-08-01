class Song(object):		#this is how we define a class with an arg

	def __init__(self,lyrics):	#instantiates the self 'Song' (instance of a class)
		self.lyrics = lyrics	#now declaring that the song has its own lyrics

	def sing_me_a_song(self):	#defining a func with self(song) as an arg
		for line in self.lyrics:	#looping for every line and printing it
			print line

happy_bday = Song(["Happy birthday to You", "I don't want to get sued", "So I'll stop right there"]);	#lyrics passed into class Song() and storing in a var

bulls_on_parade = Song(["They rally around the family","with pockets full of shells"])

happy_bday.sing_me_a_song()		#calling a func with obj passed into its class

bulls_on_parade.sing_me_a_song()
