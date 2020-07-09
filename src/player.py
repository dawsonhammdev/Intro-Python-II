
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player: 
    def __init__(self, location, backpack=[]):
        self.location = location
        self.backpack = backpack

    def __str__(self):
        return f"Location: {self.location}, Backpack: {self.backpack}"

    def status(self):
        print(f"Location: {self.location}")
        print("Backpack: ")
        for p in self.backpack:
            return p

    def add_to(self,item):
        self.backpack.append(item)
