class User():
	def __init__ (self, name, email, password, friends_list=[], posts=[]):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list=[]
		self.posts=[]

	def add_friend(self, email):
		friends_list.append(email)
		print(self.name + " added" + email + " as a friend!")

	def remove_friend(self, email):
		friends_list.remove(email)
		print(" you have tired of" + email + " and removed them as a friend!")

	def post(self, text):
		self.text = text
		self.posts.append(text)
		print(name + " has posted" + text)

	def get_userinfo(self):
		print(name)
		print(email)
		print(password)
		print(friends_list)
		print(posts)

user1 = User("Loai", "loai17@meet.mit.edu", "myhiddenpassword123")
user2 = User("shelly", "shelly@meet.mit.edu", "mypassword567")
user1.add_friend(user2.email)
user1.post("hello. my name is Loai! I like to eat toast and see the sunset on cold morning days.")
user1.get_userinfo()
user1.remove_friend(user2)


