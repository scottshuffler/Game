__author__ = 'Scott'
import character
import enemy

char = character.Character()
enemy = enemy.Enemy()

print enemy.get_health()

hp = enemy.get_health()

enemy.set_health(hp, 1000)

print enemy.get_health()