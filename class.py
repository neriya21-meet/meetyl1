class Animal(object):
	def __init__(self, sound, name, age, favorite_food):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_food = favorite_food
	def eat(self, favorite_food):
		print(" Yummy!" + self.name + " is eating" + favorite_food)

	def make_sound(self, x):
		while x is x>0:
			print( self.sound + " goes " + self.name + " when she eats " + self.favorite_food)
			x=x-1

	
	

class Person(object):
	def __init__(self, name, age, city, gender, sexuality, school, siblings, favorite_breakfast):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.sexuality = sexuality
		self.school = school
		self.siblings = siblings
	
	def breakfast(self, favorite_breakfast): 
		print(self.name + " loves to eat " + favorite_breakfast + "for breakfast ")

	def work_out(self, sports):
		print(self.name + " works out in the gym with " + sports + "three days a week! ")



person1 = Person("Charlie", 27, "Lebanon, Kansas", "Female", "Lesbian", "has finished school", 0, "cherries")



animal1 = Animal("sqweee", "Liona" , 3 , "fried_brocoli")
animal1.eat(" fried_brocoli")
animal1.make_sound(4)
person1.breakfast( "cherries ")
person1.work_out( "dumbells, weights and the treadmill ")



