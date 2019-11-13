class Animal(object);
	def _init_(self, sound, name, age, favorite_food)
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_food = favorite_food
	def eat(self, favorite_food):
		print(" Yummy!" + self.name + " is eating" + favorite_food)

animal1 = Animal("sqweee", "Liona" , 3 , "fried_brocoli")
animal1.eat()

