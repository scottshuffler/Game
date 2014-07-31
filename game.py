__authors__ = 'shuffleres, sinkdb'

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

while health != 0 and enemy_health != 0:
    userinput = raw_input("Attack or heal: ").lower()
    if userinput == "attack":
        energy -= 10
        enemy_health -= attack
    else:
        energy -= 20
        health += 30

    if enemy_health < 50000:
        enemy_energy -= 20
        enemy_health += 40
    else:
        energy -= 10
        health -= enemy_attack

    print("Your stats: ", health, energy, attack, heal)
    print("Enemy stats: ", enemy_health, enemy_energy, enemy_attack, enemy_heal)