#change and delete

class Game:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
    def show_game_info(self):
        print(f"Game name: {self.name} and game creator: {self.creator}.")
        
# let's create two objects

game_1 = Game("Counter Strike", "Counter Strike Team")

game_2 = Game("Yakalamaç", "Unknown people")

game_1.creator = "Mustafa Büyükdereli" #change

game_1.show_game_info() # Game name: Counter Strike and game creator: Mustafa Büyükdereli.

del game_1.creator

game_1.show_game_info() #AttributeError: 'Game' object has no attribute 'creator'
