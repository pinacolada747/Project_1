class Skills():
    def set_data(self, *data):
        self.name = data[0]
        self.active = data[1]
        self.probability = data[2]
        self.scaling_type = data[3]
        self.scaling = data[4]

    def show_data(self,):
        print('skill name:', self.name) #string
        print('active:',self.active) #0 or 1
        print('probability:', self.probability) # 1 to 100
        print('scaling_type:', self.scaling_type) # string
        print('scaling:', self.scaling) # 70 to 200

class Stun(Skills):
    def __init__(self,creature):
        name = 'Stun'
        active = 1
        probability = 15
        scaling_type = 'pwr'
        scaling = 150
        self.set_data(name, active, probability,scaling_type,scaling)
        creature.skill_list.append(self)

class Regeneration(Skills):
    def __init__(self,creature):
        name = 'Regeneration'
        active = 1
        probability = 50
        scaling_type = 'con'
        scaling = 150
        self.set_data(name, active, probability,scaling_type,scaling)
        self.active_rounds = round(self.scaling * creature.pwr)
        self.effect_per_round = self.scaling * creature.pwr * 3
        creature.skill_list.append(self)

class Lacerate(Skills):
    def __init__(self,creature):
        name = 'Lacerate'
        active = 1
        probability = 50
        scaling_type = 'pwr'
        scaling = 1.5
        self.set_data(name, active, probability,scaling_type,scaling)
        self.active_rounds = round(self.scaling * creature.pwr)
        self.effect_per_round = self.scaling * creature.pwr * 3
        creature.skill_list_append(self)

    #skill ideas
    # 1. stun - imobilize for 2 rounds -pwr
    # 2. incapitate - reduce damage
    # 3. revive - undead
    # 4. lacerate - DoT - str
    # 5. Theft - luck
    # 6. Riposte - deflect and parry - luck
    # 7. Health regen



