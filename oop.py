### Object Orienting Programming ¨
# what is an object?
# object has methods and attributes that we can use with DOT method
#What is the purpose of OPP? To creat our own data-type!

class PlayerCharacter :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def run(self) :
        print('run')
        return 'done!'

player1 = PlayerCharacter('Samira', 41)
player2 = PlayerCharacter('Leonard', 5)
player3 = PlayerCharacter('Charlie', 2)

print(player1.name)

## Methods & Attrbiutes
class RacingCars :
    def __init__(self, name, model, color, max_speed) :
        self.name = name # attribute
        self.model = model
        self.color = color
        self.max_speed = max_speed
    def intro(self) :
        return print(f'The {self.name} is an amazing {self.model} car.And the {self.color} is a classic.')
    
    def race(self) :
        return print(f'{self.name} is speeding to {self.max_speed}')
    
car1 = RacingCars('Ferrari',2006, 'red', '340 km/h')
car2 = RacingCars('Aston Martin',2008, 'black', '354 km/h')
car3 = RacingCars('Mercedes',2014, 'silver', '321 km/h')

car1.intro()
car2.intro()
car3.intro()

car1.race()
car2.race()
car3.race()


# Ex. The oldest cat

class Cat:
    species = 'mammal' # attribute for this class
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")

## @classmethod & @staticmethod
# are called decorators 

class PlayerId :
    membership = True #attribute
    def __init__(self, username, score) :
        self.username = username
        self.score = score
    
    @classmethod  # We do not need to instantiate objects!
    def adding_things(cls, badge1, badge2) :
        return cls('Tedy', badge1 + badge2 ) # with cls at this line we are instantiating an object
    
    #@staticmethod # Exact like @classmethod we just do not care any more about class state in this method
    #def adding_things( badge1, badge2) :
    #    return  badge1 + badge2 

player10 = PlayerId.adding_things(2,3)
print(player10.score)

## 4 PILLARS OF OOP

# ENCAPSULATION is binding of data & functions that manipulate the data

# ABSTRACTION means hiding of information or abstracting away information
# and giving access to only what's neccesary
   # Private vs Public variables

# private ? we use _varible's name to show that is a private variable
# but that has no power; it is just a convention to show to others not ot 
# over ride this variable
class Fruit :
    def __init__(self,name, color):
        self._name = name
        self._color = color
    
    def run (self):
       print('run')
    
    def speak(self):
        print(f'Hi I am {self.name} and my color is {self.color}')
    
fruit1 = Fruit('apple', 'red')
fruit2 = Fruit('banana', 'yellow')
fruit3 = Fruit('pearl', 'green')

fruit1._name = '!!!!'
fruit1.speak = 'BOOOO'

# ENHERITANCE allows new objects to take on the properties of exicting object

class User :  # parent class
    def sign_in(self): # No __init__ method; we could have it but if we do not have any variable or attributes
        print('logged in!') # that we want to assign to user, then we would not need any __init__ method

class Wizard(User) :  # children classes = sub-classes = drived-classes
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'atacking with the power of {self.power}.')

        
class Archer(User) : # children classes = sub-classes = drived-classes
    def __init__(self, name, num_arrows):
      self.name = name
      self.num_arrows = num_arrows
    
    def attack(self):
        print(f'atacking with the arrows. Number of arrows left : {self.num_arrows}')

wizard1 = Wizard('Marlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object)) # everything in python is an object so everything is instance of the base object
    
# POLYMORPHYSM allows us to have many forms

def player_attack(char):
    char.attack()

player_attack(wizard1)  
player_attack(archer1)  

for char in [wizard1, archer1]:
    char.attack()








        


    
