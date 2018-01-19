def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        attacker = fighter1
        attacked = fighter2
    else:
        attacker = fighter2
        attacked = fighter1
    while fighter1.health > 0 and fighter2.health >0:
        attacked.health -= attacker.damage_per_attack
        if attacked.health<=0:
            return attacker.name
            break
        attacked, attacker = attacker, attacked