def p_heal_disappear(hp, max_hp, status, player_heal):
    if hp <= 0:
        status = "dead"
        return status
    elif hp >= max_hp:
        hp = max_hp
        return hp
    else:
        hp += player_heal
        return hp
