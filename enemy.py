__author__ = 'shuffleres'


class Enemy:
    def __init__(self):
        self.enemy_health = 100000
        self.enemy_energy = 100
        self.enemy_attack = 100
        self.enemy_heal = 40

    def set_health(self, enemy_health, hit):
        self.enemy_health = enemy_health - hit

    def get_health(self):
        return self.enemy_health