like = []
comment = []
posts=[]

class User():
	def __init__ (self, name, email, password, friends_list = [], posts = []):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = friends_list


	def add_friend(self, f_email):
		self.friends_list.append(f_email)
		print(self.name + " added " + f_email + " as a friend!")

	def remove_friend(self, f_email):
		self.friends_list.remove(f_email)
		print(" you have tired of " + f_email + " and removed them as a friend!")

	def post(self, text,comment,likes):
		self.text=text
		self.comment=comment
		self.likes=likes
		post1=Post(text,comment,likes)
		posts.append(post1)

	def get_userinfo(self):
		print(self.name)
		print(self.email)
		print(self.password)
		print(self.friends_list)
		print(posts)

class Post():
	def __init__ (self, text):
		self.text = text
		self.likes = 0

	def F_comment(self,f_email,text):
		comment1=Comment(text, f_email, self)
		Comment.append(comment1)
		print(f_email +  "has deighned to comment on"  + email + " wretched post")
		print(comment.len)
	
	def F_likes(self):
		self.like++
		print(f_email + "has bestowed their favor on " + email + ". Be Happy!")
		# print( like.len)




class Comment(Post):
	def __init__ (self, text, f_email, post):
		Post.__init__(self, text)
		self.f_email = f_email
		self.post = post


	def delete_comment(self):
		comment.remove(comment)
	
	def edit_comment(self, n_text):
		comment.remove(self.text)
		comment.append(n_text)
		print( " Your last comment was a nightmare! Thank god you edited it!!!" )





user1 = User("Loai", "loai17@meet.mit.edu", "myhiddenpassword123")
user2 = User("shelly", "shelly@meet.mit.edu", "mypassword567")
user1.add_friend(user2.email)
user1.post(" Hello, I humbly request your attention",'ok',3)
user1.get_userinfo()
user1.remove_friend(user2.email)

Comment.add_comment(" Nice shoes babe!")