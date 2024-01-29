from Inventory import Inventory

class Character:
    def __init__(self, hero_type):
        self.hero_type = hero_type
        self.attack = 0
        self.health = 0
        self.speed = 0
        self.inventory = None

    def set_attributes(self):
        if self.hero_type == "A":  # Archer
            self.attack = 7
            self.health = 5
            self.speed = 10
        elif self.hero_type == "W":  # Warrior
            self.attack = 7
            self.health = 10
            self.speed = 5
        else:
            print("Invalid choice. Please try again.")

    def display_attributes(self):
        print("Character created!")
        print("Hero Type:", self.hero_type)
        print("Attack:", self.attack)
        print("Health:", self.health)
        print("Speed:", self.speed)

    def assign_inventory(self):
        self.inventory = Inventory(self.hero_type)

    
        