class Game:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
    def show_game_info(self):
        print(f"Game name: {self.name} and game creator: {self.creator}.")
        
# let's create two objects

game_1 = Game("Counter Strike", "Counter Strike Team")

game_2 = Game("Yakalamaç", "Unknown people")

print(game_1.name) # Counter Strike

print(game_2.creator) # Unknown people
