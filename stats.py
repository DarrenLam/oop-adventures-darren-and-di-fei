def Physical_Power(strength):
    physical_power = strength

def Physical_Power_Bonus(physical_power):
    physical_power_bonus = 0.2
    if physical_power > 100:
        physical_power = 100
    if physical_power < 0:
        physical_power = 0
    while physical_power > 50:
        physical_power_bonus = physical_power_bonus + 0.005
        physical_power = physical_power - 1
    while physical_power > 15:
        physical_power_bonus = physical_power_bonus + 0.01
        physical_power = physical_power - 1
    while physical_power > 11:
        physical_power_bonus = physical_power_bonus + 0.02
        physical_power = physical_power - 1
    while physical_power > 7:
        physical_power_bonus = physical_power_bonus + 0.03
        physical_power = physical_power - 1
    while physical_power > 5:
        physical_power_bonus = physical_power_bonus + 0.05
        physical_power = physical_power - 1
    while physical_power > 0:
        physical_power_bonus = physical_power_bonus + 0.1
        physical_power = physical_power - 1
    round(physical_power_bonus,3)

def Max_Health(strength):
    max_health = 60
    if strength > 100:
        strength = 100
    if strength < 0:
        strength = 0
    while strength > 75:
        max_health = max_health + 0.5
        strength = strength - 1
    while strength > 50:
        max_health = max_health + 1
        strength = strength - 1
    while strength > 10:
        max_health = max_health + 2
        strength = strength - 1
    while strength > 0:
        max_health = max_health + 3
        strength = strength - 1
    print(max_health)

def Action_Speed(agility):
    action_speed = 0.62
    if agility > 100:
        agility = 100
    if agility < 0:
        agility = 0
    while agility > 50:
        action_speed = action_speed + 0.005
        agility = agility - 1
    while agility > 41:
        action_speed = action_speed + 0.01
        agility = agility - 1
    while agility > 25:
        action_speed = action_speed + 0.015
        agility = agility - 1
    while agility > 13:
        action_speed = action_speed + 0.01
        agility = agility - 1
    while agility > 10:
        action_speed = action_speed + 0.02
        agility = agility - 1
    while agility > 0:
        action_speed = action_speed + 0.03
        agility = agility - 1
    round(action_speed,3)
    print(action_speed)

Action_Speed(50)