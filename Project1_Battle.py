from Project1_Creature import *
from Project1_Hero import *
from Project1_Monsters import *
from Project1_Skills import *

def crit_chance(crit, atk):
    a = random.randint(1, 100)
    b = random.randint(80, 120)
    if a > crit:
        return (atk * b) / 100
    elif a <= crit:
        time.sleep(0.6)
        print('it is a critical hit')
        return (atk * b * 2) / 100

def damage(a_crit, a_atk, d_dfc):
    damage = round(crit_chance(a_crit, (a_atk - a_atk * d_dfc)))
    return damage

def battle_choice():
    while True:
        print('-' * 50)
        battle_choice = input('will you fight or run ?')
        print('-' * 50)
        if battle_choice == 'fight':
            print('-' * 50)
            print('you will fight like a man')
            print('-' * 50)
            return True

        elif battle_choice == 'run':
            print('-' * 50)
            print('you run for your life')
            print('-' * 50)
            return False

        else:
            print('please choose fight or run')


class Battle():
    def __init__(self,hero,monster):
        hero.combat_initialize()
        monster.monster_combat_initialize()
        h_name = hero.return_name()
        h_hp = hero.return_current_hp()
        h_atk = hero.return_atk()
        h_dfc = hero.return_dfc_rate()
        h_crit = hero.return_crit()
        h_luc = hero.return_luc()
        m_name = monster.return_name()
        m_race = monster.return_race()
        m_hp = monster.return_current_hp()
        m_atk = monster.return_atk()
        m_dfc = monster.return_dfc_rate()
        m_crit = monster.return_crit()
        m_luc = monster.return_luc()
        # monster.skill_list[0].show_data

        print('-' * 20, 'combat mode', '-' * 20)

        turn = 2
        while True:
            if turn == 2:
                if h_luc > m_luc:
                    turn = 0
                    print(h_name, 'managed to sneak up on', m_name, 'the', m_race)
                    monster.print_icon()
                elif m_luc > h_luc:
                    turn = 1
                    print(h_name, 'You have been ambushed by ', m_name, 'the', m_race)
                    monster.print_icon()
            elif turn == 0:
                turn = 1
                time.sleep(0.5)
                print(h_name,'attacks')
                m_hp -= damage(h_crit,h_atk,m_dfc)
                time.sleep(0.6)
                print(h_name, ' have caused', damage(h_crit,h_atk,m_dfc), 'damage to ', m_name, 'the', m_race, ' have', m_hp, 'left')
                print('-' * 50)
                if m_hp < 0:
                    hero.set_current_hp(h_hp)
                    hero.soul_absorb(m_race)
                    print('You have won the fight with', hero.return_current_hp(), 'health remaining')
                    monster.set_dead_or_alive('0')
                    break
            elif turn == 1:
                turn = 0
                time.sleep(0.6)
                print('Monster attacks')
                h_hp -= damage(m_crit,m_atk,h_dfc)
                print(m_name, 'the', m_race, 'have caused', damage(m_crit,m_atk,h_dfc), 'damage to the hero have', h_hp, 'hp left')
                print('-' * 50)
                if h_hp < 0:
                    time.sleep(1)
                    print('YOU HAVE DIED')
                    time.sleep(2)
                    quit()


def main():
    def hero_start():
        hero1 = Hero()
        print('-' * 100)
        print('You have entered character creation')
        print('-' * 100)
        time.sleep(0.8)
        hero1.show_data()
        hero1.set_current_hp(int(hero1.return_con() * 25))

        return hero1

    def ogre_start():
        ogre1 = Ogre()
        ogre1.ogre_start()
        return ogre1

    hero1 = hero_start()
    ogre1 = ogre_start()
    ogre1.skill_list_append(Lacerate(ogre1))


    Battle(hero1,ogre1)

if __name__ == '__main__':
    main()