class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self,first_name , last_name , treats , pet_food , pet):
        self.first_name=first_name
        self.last_name=last_name
        self.pet=pet
        self.treats=treats
        self.pet_food=pet_food
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print(f"{self.pet.name} is playing now")
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        print(f"{self.pet.name} is eating now")
        return self
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self


class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self,name , type , tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=100
        self.energy=20
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy+=25
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy+=5
        self.health+=10
# play() - increases the pet's health by 5
    def play(self):
        self.health+=5
# noise() - prints out the pet's sound
    def noise(self):
        print(f"the made a soun {self.tricks}")

sasuke=Ninja("sasuke","Uchiha","white","chewy",Pet("jrana","frog","meow"))
sasuke.feed().bathe().walk()