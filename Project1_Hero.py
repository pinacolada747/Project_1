from Project1_Creature import *
import time
import random

def stat_randomize():
    while True:
        a = random.randint(1, 7)
        b = random.randint(1, 7)
        c = random.randint(1, 7)
        d = random.randint(1, 7)
        if a + b + c + d == 20:
            return a, b, c, d

class Hero(Creature):

    def __init__(self):
        time.sleep(1)
        print('-' * 100)
        print('You have entered character creation')
        print('-' * 100)
        time.sleep(1)
        x = 3
        h_name = input('Please input hero name : ')
        time.sleep(1)
        if h_name == 'super':
            self.set_data(h_name,'fkn ute',12,12,12,12)
        else:
            h_race = 'human'
            print('-'*100)
            z = input('Type roll to determine for your stats : ')
            print('-'*100)
            while x == 3:
                if z == 'roll':
                    a,b,c,d = stat_randomize()
                    print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                    x -= 1
                    while x!= 0:
                        print('You have', x, 'more  rolls,', end = '')
                        roll_choice = input(' would you like to reroll : (yes/no) ')
                        print('-' * 100)
                        if roll_choice == 'yes':
                            x -= 1
                            a,b,c,d, = stat_randomize()
                            print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                            print('-' * 100)
                        elif roll_choice == 'no':
                            print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                            self.set_data(h_name, h_race, a,b,c,d)
                            print('-' * 100)
                            break
                        else:
                            print('please type yes or no : ')
                            continue
                        self.set_data(h_name, h_race, a, b, c, d)
                else:
                    print('-' * 100)
                    print('How difficult is it to type the word roll :')
                    a,b,c,d, = stat_randomize()
                    print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                    print('-' * 100)
                    x -= 1
                    while x!= 0:
                        print('-' * 100)
                        print('You have', x, 'more rolls', end = '')
                        g = input(',would you like to reroll (yes/no) : ')
                        print('-' * 100)
                        if g == 'yes':
                            x -= 1
                            a,b,c,d, = stat_randomize()
                            print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                            print('-'*100)
                        elif g == 'no':
                            print('Constitution:',a,'Power',b,'Luck:',c,'Defence:',d)
                            self.set_data(h_name, h_race, a,b,c,d)
                            print('-' * 100)
                            break
                        else:
                            print('Please type yes or no')
                            continue

    # access methods

    def return_name(self):
        return(self.name)

    def set_current_hp(self, h_current_hp):
        self.current_hp = h_current_hp
        print(self.return_name(),'\'s current hp is',h_current_hp)

    def return_current_hp(self):
        return(self.current_hp)

    def combat_initialize(self):
        # constitution to hp conversion
        self.current_hp = self.return_con()*25
        # power to attack conversion
        self.atk = self.return_pwr()*4.5
        # critical chance calculation
        self.crit = self.return_luc()*2.5
        # defence rating conversion
        self.dfc_rate = self.return_dfc()/20
        print('Hero HP:', self.current_hp, 'Hero Attack: ', self.atk, "Hero crit chance: ", self.crit, "Hero defence:", self.dfc_rate)
        return self.return_name(),self.current_hp, self.atk, self.crit, self.dfc_rate

    def return_atk(self):
        return(self.atk)
    def return_dfc_rate(self):
        return(self.dfc_rate)
    def return_crit(self):
        return(self.crit)

    def soul_absorb(self,monster_fought):
        greater_lesser = random.randint(0,100)
        if greater_lesser > 70:
            if monster_fought == 'orc':
                time.sleep(1)
                print('-' * 50)
                print('you have captured the greater soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.pwr += 2
                self.show_data()
            elif monster_fought == 'undead':
                pass
            elif monster_fought == 'dark_elf':
                time.sleep(1)
                print('-' * 50)
                print('you have captured the greater soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.dfc += 2
                self.show_data()
            elif monster_fought == 'ogre':
                time.sleep(1)
                print('-' * 50)
                print('you have captured the greater soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.con += 2
                self.current_hp += 50
                self.show_data()
            elif monster_fought == 'goblin':
                time.sleep(1)
                print('-' * 50)
                print('you have captured the greater soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.luc += 2
                self.show_data()
        else:

            if monster_fought == 'orc':
                time.sleep(1)
                print('-' * 50)
                print('you have captured the lesser soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.pwr += 1
                self.show_data()
            elif monster_fought == 'undead':
                pass
            elif monster_fought == 'dark_elf':
                time.sleep(1)
                print('-' * 50)
                print('you have captured the lesser soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.dfc += 1
                self.show_data()
            elif monster_fought == 'ogre':
                time.sleep(1)
                print('-' * 50)
                print('you have captured lesser soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.con += 1
                self.current_hp += 25
                self.show_data()
            elif monster_fought == 'goblin':
                time.sleep(1)
                print('-' * 50)
                print('you have captured the lesser soul of the ', monster_fought)
                print('-' * 50)
                time.sleep(1)
                self.luc += 1
                self.show_data()



def main():
    hero1 = Hero()
    hero1.show_data

if __name__ == '__main__':
    main()