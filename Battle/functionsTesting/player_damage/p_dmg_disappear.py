def p_dmg_disappear(status, hp, enemy_dmg):
    hp -= enemy_dmg
    if hp <= 0:
        status = "dead"
        return status
    else:
        return hp
