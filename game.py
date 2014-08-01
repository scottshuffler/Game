__authors__ = 'shuffleres, sinkdb'

from character import Character

round_count = 0

char = Character()

print("Your stats: ", health, energy, attack, heal)
print("Enemy stats: ", enemy_health, enemy_energy, enemy_attack, enemy_heal)

while char.health > 0 and enemy_health > 0:
    user_input = raw_input("Attack or heal: ").lower()

    '''user turn'''
    if user_input == "attack":
        energy -= 10
        enemy_health -= attack
    else:
        energy -= 20
        health += 30

    '''Enemy turn'''
    if enemy_health < 50000:
        enemy_energy -= 20
        enemy_health += 40
    else:
        enemy_energy -= 10
        health -= enemy_attack

    '''Even rounds gain 20 energy'''
    if round_count % 2 == 0:
        enemy_energy += 10
        energy += 10

    '''Print stats'''
    print("Your health:", health, "Your energy: ", energy)
    print("Enemy health: ", enemy_health, "Your energy: ", enemy_energy)

    '''Update round count'''
    round_count += 1

if health >= 0:
    print("You win")
else:
    print("You lose")
