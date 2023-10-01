### Object Orienting Programming ¨
# what is an object?
# object has methods and attributes that we can use with DOT method
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


        


    