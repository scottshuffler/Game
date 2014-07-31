__authors__ = 'shuffleres, sinkdb'

round_count = 0

''''Character'''
health = 100000
energy = 100
attack = 150
heal = 30

'''Enemy'''
enemy_health = 100000
enemy_energy = 100
enemy_attack = 100
enemy_heal = 40

print("Your stats: ", health, energy, attack, heal)
print("Enemy stats: ", enemy_health, enemy_energy, enemy_attack, enemy_heal)

while health > 0 and enemy_health > 0:
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
        enemy_energy += 20
        energy += 20

    '''Print stats'''
    print("Your stats: ", health, energy, attack, heal)
    print("Enemy stats: ", enemy_health, enemy_energy, enemy_attack, enemy_heal)

if health >= 0:
    print("You win")
else:
    print("You lose")