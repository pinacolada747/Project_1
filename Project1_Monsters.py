from Project1_Creature import *
import random
import time

class Monster(Creature):

    def monster_combat_initialize(self):
        self.current_hp = self.return_con()*20
        self.atk = self.return_pwr()*3
        self.crit = self.return_luc()*2
        self.dfc_rate = self.return_dfc()/20
        print('Monster HP:', self.current_hp, 'Monster Attack: ', self.atk, "Monster crit chance: ", self.crit, "Monster defence:",
        self.dfc_rate)
        return self.return_name(),self.return_race(),self.current_hp, self.atk, self.crit, self.dfc_rate
    def print_name(self):
        print(self.name,'the',self.race)
    def return_atk(self):
        return(self.atk)
    def return_dfc_rate(self):
        return(self.dfc_rate)
    def return_crit(self):
        return(self.crit)
    def return_current_hp(self):
        return(self.current_hp)

    def skill_list_append(self,a):
        self.skill_list.append(a)

#Coordinates
    def set_coordinate(self,y,x):
        self.y_value = y
        self.x_value = x

    def return_y_coordinate(self):
        return(self.y_value)
    def return_x_coordinate(self):
        return(self.x_value)

    def show_coordinates(self):
        print(self.y_value,self.x_value)


#Monster class initiate

class Ogre(Monster):

    def ogre_start(self):
        ogre_name_list = ['Stonehead','Stonebrain','Thick']
        ogre_name = random.choice(ogre_name_list)
        ogre_race = 'ogre'
        ogre_con = random.randint(4,6)
        ogre_pwr = random.randint(4,6)
        ogre_dfc = random.randint(1,3)
        ogre_luc = random.randint(0,3)
        self.set_data(ogre_name, ogre_race, ogre_con,ogre_pwr,ogre_dfc,ogre_luc)
        self.icon = 'ascii_ogre'

    def print_icon(self):
        f = open(self.icon,'r')
        print(''.join([g for g in f]))

class Undead(Monster):
    def undead_start(self):
        undead_name_list = ['Brittle','Tibia','Themer']
        undead_name = random.choice(undead_name_list)
        undead_race = 'undead'
        undead_con = random.randint(4,8)
        undead_pwr = random.randint(1,3)
        undead_dfc = random.randint(4,4)
        undead_luc = random.randint(0,1)
        self.set_data(undead_name, undead_race, undead_con,undead_pwr,undead_dfc,undead_luc)
        self.icon = 'ascii_undead.txt'

    def print_icon(self):
        f = open(self.icon, 'r')
        print(''.join([g for g in f]))

class Goblin(Monster):
    def goblin_start(self):
        goblin_name_list = ['Snitch','Ratnose','Shwifty']
        goblin_name = random.choice(goblin_name_list)
        goblin_race = 'goblin'
        goblin_con = random.randint(1,4)
        goblin_pwr = random.randint(1,3)
        goblin_dfc = random.randint(4,6)
        goblin_luc = random.randint(6,9)
        self.set_data(goblin_name, goblin_race, goblin_con,goblin_pwr,goblin_dfc,goblin_luc)
        self.icon = 'ascii_undead.txt'

    def print_icon(self):
        f = open(self.icon, 'r')
        print(''.join([g for g in f]))
class Orc(Monster):
    def orc_start(self):
        orc_name_list = ['Bloodmane','Teethbreaker','Curbstomp']
        orc_name = random.choice(orc_name_list)
        orc_race = 'orc'
        orc_con = random.randint(3,5)
        orc_pwr = random.randint(4,6)
        orc_dfc = random.randint(2,3)
        orc_luc = random.randint(2,4)
        self.set_data(orc_name, orc_race, orc_con,orc_pwr,orc_dfc,orc_luc)
        self.icon = 'ascii_ogre'

    def print_icon(self):
        f = open(self.icon, 'r')
        print(''.join([g for g in f]))
class Dark_elf(Monster):

    def dark_elf_start(self):
        dark_elf_name_list = ['Kabip','Lanik','Wadeep']
        dark_elf_name = random.choice(dark_elf_name_list)
        dark_elf_race = 'dark elf'
        dark_elf_con = random.randint(2,5)
        dark_elf_pwr = random.randint(3,5)
        dark_elf_dfc = random.randint(1,3)
        dark_elf_luc = random.randint(1,9)
        self.set_data(dark_elf_name, dark_elf_race, dark_elf_con,dark_elf_pwr,dark_elf_dfc,dark_elf_luc)
        self.icon = 'ascii_undead.txt'

    def print_icon(self):
        f = open(self.icon, 'r')
        print(''.join([g for g in f]))
    
def ogre_start():
    ogre1 = Ogre()
    ogre1.ogre_start()
    return ogre1

def undead_start():
    undead1 = Undead()
    undead1.undead_start()
    return undead1


def goblin_start():
    goblin1 = Goblin()
    goblin1.goblin_start()
    return goblin1

def dark_elf_start():
    dark_elf1 = Dark_elf()
    dark_elf1.dark_elf_start()
    return dark_elf1

def orc_start():
    orc1 = Orc()
    orc1.orc_start()
    return orc1

def monster_line_up():
    global lineup_list
    lineup_list = []
    for x in range(5):
        monster_tick = random.randint(0,4)
        if monster_tick == 0:
            ogre_start()
            lineup_list.append(ogre_start())
        elif monster_tick == 1:
            undead_start()
            lineup_list.append(undead_start())
        elif monster_tick == 2:
            goblin_start()
            lineup_list.append(goblin_start())
        elif monster_tick == 3:
            orc_start()
            lineup_list.append(orc_start())
        elif monster_tick == 4:
            dark_elf_start()
            lineup_list.append(dark_elf_start())

    return lineup_list

# def monster_allocation():
#     global lineup_list, y_list, x_list
#     y_list = []
#     x_list = []
#     for ll in range(len(lineup_list)):
#         y1 = random.randint(0,9)
#         y_list.append(y1)
#         x1 = random.randint(0,9)
#         x_list.append(x1)
#     for ll2 in range(len(lineup_list)):
#         print('Monster',ll2,'is at Y:', y_list[ll2],'X:',x_list[ll2])
#         return y_list, x_list

#need to address recurring location - done

#sort lineuplist
monster_line_up()


