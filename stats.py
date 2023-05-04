def Physical_Power(strength):
    if strength > 100:
        strength = 100
    if strength < 0:
        strength = 0
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

def Move_Speed(agility):
    move_speed = -30
    if agility > 100:
        agility = 100
    if agility < 0:
        agility = 0
    while agility > 65:
        move_speed = move_speed + 1/3
        agility = agility - 1
    while agility > 45:
        move_speed = move_speed + 0.5
        agility = agility - 1
    while agility > 15:
        move_speed = move_speed + 1
        agility = agility - 1
    while agility > 0:
        move_speed = move_speed + 2
        agility = agility - 1
    
def Item_Equip_Speed(agility):
    item_equip_speed = 0.05
    if agility > 100:
        agility = 100
    if agility < 0:
        agility = 0
    while agility > 70:
        item_equip_speed = item_equip_speed + 0.01
        agility = agility - 1
    while agility > 35:
        item_equip_speed = item_equip_speed + 0.02
        agility = agility - 1
    while agility > 15:
        item_equip_speed = item_equip_speed + 0.05
        agility = agility - 1
    while agility > 2:
        item_equip_speed = item_equip_speed + 0.07
        agility = agility - 1
    while agility > 1:
        item_equip_speed = item_equip_speed + 0.04
        agility = agility - 1
    while agility > 0:
        item_equip_speed = item_equip_speed + 0
        agility = agility - 1

def Magic_Power(will):
    if will > 100:
        will = 100
    if will < 0:
        will = 0
    magic_power = will

def Magic_Power_Bonus(magic_power):
    magic_power_bonus = 0.1
    if magic_power > 100:
        magic_power = 100
    if magic_power < 0:
        magic_power = 0
    while magic_power > 50:
        magic_power_bonus = magic_power_bonus + 0.005
        magic_power = magic_power - 1
    while magic_power > 40:
        magic_power_bonus = magic_power_bonus + 0.01
        magic_power = magic_power - 1
    while magic_power > 25:
        magic_power_bonus = magic_power_bonus + 0.02
        magic_power = magic_power - 1
    while magic_power > 15:
        magic_power_bonus = magic_power_bonus + 0.03
        magic_power = magic_power - 1
    while magic_power > 5:
        magic_power_bonus = magic_power_bonus + 0.05
        magic_power = magic_power - 1
    while magic_power > 1:
        magic_power_bonus = magic_power_bonus + 0.1
        magic_power = magic_power - 1
    while magic_power > 0:
        magic_power_bonus = magic_power_bonus + 0
        magic_power = magic_power - 1

def Magic_Resistance(will):
    magic_resistance = -20
    if will > 100:
        will = 100
    if will < 0:
        will = 0
    while will > 94:
        magic_resistance = magic_resistance + 0.5
        will = will - 1
    while will > 92:
        magic_resistance = magic_resistance + 1
        will = will + 1
    while will > 91:
        magic_resistance = magic_resistance - 1
        will  = will - 1
    while will > 65:
        magic_resistance = magic_resistance + 0.5
        will = will - 1
    while will > 55:
        magic_resistance = magic_resistance + 1
        will = will - 1
    while will > 35:
        magic_resistance = magic_resistance + 2
        will = will - 1
    while will > 5:
        magic_resistance = magic_resistance + 3
        will = will - 1
    while will > 0:
        magic_resistance = magic_resistance + 4
        will = will - 1

def Magical_Damage_Reduction(magic_resistance):
    magical_damage_reduction = -4.95
    if magic_resistance > 500:
        magic_resistane = 500
    if magic_resistance < -300:
        magic_resistance = -300
    while magic_resistance > 350:
        magical_damage_reduction = magical_damage_reduction + 0.001
        magic_resistance = magic_resistance - 1
    while magic_resistance > 250:
        magical_damage_reduction = magical_damage_reduction + 0.002
        magic_resistance = magic_resistance - 1
    while magic_resistance > 150:
        magical_resistance_reduction = magical_resistance_reduction + 0.003
        magic_resistance = magic_resistance - 1
    while magic_resistance > 100:
        magical_damage_reduction = magical_damage_reduction + 0.002
        magic_resistance = magic_resistance - 1
    while magic_resistance > 50:
        magical_damage_reduction = magical_damage_reduction + 0.001
        magic_resistance = magic_resistance - 1
    while magic_resistance > 40:
        magical_damage_reduction = magical_damage_reduction + 0.002
        magic_resistance = magic_resistance - 1
    while magic_resistance > 30:
        magical_damage_reduction = magical_damage_reduction + 0.003
        magic_resistance = magic_resistance - 1
    while magic_resistance > 19:
        magical_damage_reduction = magical_damage_reduction + 0.004
        magic_resistance = magic_resistance - 1
    while magic_resistance > 10:
        magical_damage_reduction = magical_damage_reduction + 0.005
        magic_resistance = magic_resistance - 1
    while magic_resistance > -15:
        magical_damage_reduction = magical_damage_reduction + 0.01
        magic_resistance = magic_resistance - 1
    while magic_resistance > -300:
        magical_damage_reduction = magical_resistance_reduction + 0.02
        magic_resistance = magic_resistance - 1

def Buff_Duration(will):
    buff_duration = 0.2
    if will > 100:
        will = 100
    if will < 0:
        will = 0
    while will > 50:
        buff_duration = buff_duration + 0.005
        will = will - 1
    while will > 15:
        buff_duration = buff_duration + 0.01
        will = will - 1
    while will > 11:
        buff_duration = buff_duration + 0.02
        will = will - 1
    while will > 7:
        buff_duration = buff_duration + 0.03
        will = will - 1
    while will > 5:
        buff_duration = buff_duration + 0.05
        will = will - 1
    while will > 0:
        buff_duration = buff_duration + 0.1
        will = will - 1

def Debuff_Duration(will):
    if will > 100:
        will = 100
    if will < 0:
        will = 0
    debuff_duration_list = [5,3.3,2.5,2,1.667,1.429,1.333,1.25,1.205,1.163,1.124,1.087,1.064,1.042,1.02,1,0.98,0.971,0.962,0.952,0.943,0.935,0.926,0.917,0.907,0.897,0.887,0.877,0.87,0.862,0.855,0.847,0.84,0.833,0.826,0.82,0.813,0.806,0.8,0.794,0.787,0.781,0.775,0.769,0.763,0.758,0.752,0.746,0.741,0.738,0.735,0.733,0.73,0.727,0.725,0.722,0.719,0.717,0.714,0.712,0.709,0.707,0.704,0.702,0.699,0.697,0.694,0.692,0.69,0.687,0.685,0.683,0.68,0.678,0.676,0.673,0.671,0.669,0.667,0.664,0.662,0.66,0.658,0.656,0.654,0.651,0.649,0.647,0.645,0.643,0.641,0.639,0.637,0.635,0.633,0.631,0.629,0.627,0.625]
    debuff_duration = debuff_duration_list[will]

def Spell_Casting_Speed(knowledge):
    spell_casting_speed = 0.05
    if knowledge > 100:
        knowledge = 100
    if knowledge < 0:
        knowledge = 0
    while knowledge > 40:
        spell_casting_speed = spell_casting_speed + 0.02
        knowledge = knowledge - 1
    while knowledge > 30:
        spell_casting_speed = spell_casting_speed + 0.03
        knowledge = knowledge - 1
    while knowledge > 1:
        spell_casting_speed = spell_casting_speed + 0.05
        knowledge = knowledge - 1
    while knowledge > 0:
        spell_casting_speed = spell_casting_speed + 0
        knowledge = knowledge - 1

def Magical_Interaction_Speed(knowledge):
    magical_interaction_speed = 0.25
    if knowledge > 100:
        knowledge = 100
    if knowledge < 0:
        knowledge = 0
    while knowledge > 86:
        magical_interaction_speed = magical_interaction_speed + 0.02
        knowledge = knowledge - 1
    while knowledge > 85:
        magical_interaction_speed = magical_interaction_speed + 0.03
        knowledge = knowledge - 1
    while knowledge > 84:
        magical_interaction_speed = magical_interaction_speed + 0.01
        knowledge = knowledge - 1
    while knowledge > 35:
        magical_interaction_speed = magical_interaction_speed + 0.02
        knowledge = knowledge - 1
    while knowledge > 25:
        magical_interaction_speed = magical_interaction_speed + 0.05
        knowledge = knowledge - 1
    while knowledge > 15:
        magical_interaction_speed = magical_interaction_speed + 0.07
        knowledge = knowledge - 1
    while knowledge > 0:
        magical_interaction_speed = magical_interaction_speed + 0.05
        knowledge = knowledge - 1

def Spell_Capacity(knowledge):
    if knowledge > 100:
        knowledge = 100
    if knowledge < 0:
        knowledge = 0
    spell_capacity = knowledge

def Interaction_Speed(resourcefulness):
    interaction_speed = 0.25
    if resourcefulness > 100:
        resourcefulness = 100
    if resourcefulness < 0:
        resourcefulness = 0
    while resourcefulness > 86:
        interaction_speed = interaction_speed + 0.02
        resourcefulness = resourcefulness - 1
    while resourcefulness > 85:
        interaction_speed = interaction_speed + 0.03
        resourcefulness = resourcefulness - 1
    while resourcefulness > 84:
        interaction_speed = interaction_speed + 0.01
        resourcefulness = resourcefulness - 1
    while resourcefulness > 35:
        interaction_speed = interaction_speed + 0.02
        resourcefulness = resourcefulness - 1
    while resourcefulness > 25:
        interaction_speed = interaction_speed + 0.05
        resourcefulness = resourcefulness - 1
    while resourcefulness > 15:
        interaction_speed = interaction_speed + 0.07
        resourcefulness = resourcefulness - 1
    while resourcefulness > 0:
        interaction_speed = interaction_speed + 0.05
        resourcefulness = resourcefulness - 1

def Physical_Damage_Reduction(armor_rating):
    physical_damage_reduction = -4.95
    if armor_rating > 500:
        armor_rating = 500
    if armor_rating < -300:
        armor_rating = -300
    while armor_rating > 350:
        physical_damage_reduction = physical_damage_reduction + 0.001
        armor_rating = armor_rating - 1
    while armor_rating > 250:
        physical_damage_reduction = physical_damage_reduction + 0.002
        armor_rating = armor_rating - 1
    while armor_rating > 150:
        physical_damage_reduction = physical_damage_reduction + 0.003
        armor_rating = armor_rating - 1
    while armor_rating > 100:
        physical_damage_reduction = physical_damage_reduction + 0.002
        armor_rating = armor_rating - 1
    while armor_rating > 50:
        physical_damage_reduction = physical_damage_reduction + 0.001
        armor_rating = armor_rating - 1
    while armor_rating > 40:
        physical_damage_reduction = physical_damage_reduction + 0.002
        armor_rating = armor_rating - 1
    while armor_rating > 30:
        physical_damage_reduction = physical_damage_reduction + 0.003
        armor_rating = armor_rating - 1
    while armor_rating > 19:
        physical_damage_reduction = physical_damage_reduction + 0.004
        armor_rating = armor_rating - 1
    while armor_rating > 10:
        physical_damage_reduction = physical_damage_reduction + 0.005
        armor_rating = armor_rating - 1
    while armor_rating > -15:
        physical_damage_reduction = physical_damage_reduction + 0.01
        armor_rating = armor_rating - 1
    while armor_rating > -300:
        physical_damage_reduction = physical_damage_reduction + 0.02
        armor_rating = armor_rating - 1

