class Creature():
    def set_data(self, *data):
        self.name = data[0]
        self.race = data[1]
        self.con = data[2]
        self.pwr = data[3]
        self.dfc = data[4]
        self.luc = data[5]
        self.skill_list = []

    def show_data(self):
        print('Name:', self.name)
        print('Race:', self.race)
        print('Constitution',self.con)
        print('Power:', self.pwr)
        print('Defence:',self.dfc)
        print('Luck:', self.luc)

    def return_name(self):
        return(self.name)
    def return_race(self):
        return(self.race)
    def return_con(self):
        return(self.con)
    def return_pwr(self):
        return(self.pwr)
    def return_dfc(self):
        return(self.dfc)
    def return_luc(self):
        return(self.luc)

    def set_dead_or_alive(self,status):
        self.dead_or_alive = status

    def return_dead_or_alive(self):
        return self.dead_or_alive
