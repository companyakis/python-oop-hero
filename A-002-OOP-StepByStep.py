#str method

class Game:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
    def __str__(self):
        return f"Game name: {self.name} and game creator: {self.creator}."
    

# let's create two objects

game_1 = Game("Counter Strike", "Counter Strike Team")

game_2 = Game("Yakalamaç", "Unknown people")

print(game_1)
print(game_2)

"""
Game name: Counter Strike and game creator: Counter Strike Team.
Game name: Yakalamaç and game creator: Unknown people.

"""
