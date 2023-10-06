class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def shout(self):
        print(f'{self.name} is shouting')
    
player1 = Player('Samira', 41)
player1.shout()
  

