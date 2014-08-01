__author__ = 'shuffleres'


class Character:
    def __init__(self):
        self.health = 100000
        self.energy = 100
        self.attack = 150
        self.heal = 30

    @property
    def health(self):
        return self.health

    @health.setter
    def health(self, hit):
        self.health = self.health