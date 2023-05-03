def Physical_Power(strength):
    physical_power = strength

def Physical_Power_Bonus(physical_power):
    physical_power_bonus = 0.2
    if physical_power > 100:
        physical_power = 100
    while physical_power > 0:
    if physical_power > 50:
        physical_power_bonus = physical_power_bonus + 0.005
        physical_power = physical_power - 1