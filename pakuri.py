class Pakuri:
    def __init__(self, species):  # the stats are based off of the name, so those can be initialized
        self.species = species
        self.attack = int((len(self.species) * 7) + 9)
        self.defense = int((len(self.species) * 5) + 17)
        self.speed = int((len(self.species) * 6) + 13)

    def get_species(self):  # redundant
        return self.species

    def get_attack(self):  # redundant
        return self.attack

    def get_defense(self):  # redundant
        return self.defense

    def get_speed(self):  # redundant
        return self.speed

    def set_attack(self, new_attack):  # unused; likely for zybooks checking
        self.attack = new_attack
        return self.attack

    def evolve(self):  # simple method for changing the stats the same way when evolving a pakuri species
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
