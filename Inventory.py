class Inventory:
    def __init__(self, hero_type):
        self.hero_type = hero_type
        self.items = []
        self.initialize_inventory()

    def initialize_inventory(self):
        if self.hero_type == "A":  # Archer
            self.items.append("Bow")
            self.items.extend(["Arrows"] * 10)
            self.items.extend(["Gold"] * 7)
        elif self.hero_type == "W":  # Warrior
            self.items.append("Sword")
            self.items.extend(["Gold"] * 7)

    def display_inventory(self):
        print("Inventory for", self.hero_type)
        print("Items:", ", ".join(self.items))
