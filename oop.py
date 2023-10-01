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


    
