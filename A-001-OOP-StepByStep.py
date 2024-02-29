class Game:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
    def show_game_info(self):
        print(f"Game name: {self.name} and game creator: {self.creator}.")
        
# let's create two objects

game_1 = Game("Counter Strike", "Counter Strike Team")

game_2 = Game("Yakalamaç", "Unknown people")

# call show game info

game_1.show_game_info()

game_2.show_game_info()

"""
Game name: Counter Strike and game creator: Counter Strike Team.
Game name: Yakalamaç and game creator: Unknown people.
"""
