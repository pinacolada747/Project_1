from Project1_Terrain import *
from Project1_Hero import *
from Project1_Monsters import *
from Project1_Battle import *
import time


def print_ascii(fn):
    f= open(fn,'r')
    f1 = ''.join([g for g in f])
    print_counter = 0
    for i in f1:
        if (print_counter % 101) == 0:
            time.sleep(0.1)
            print(i,end='')
            print_counter += 1
        else:
            print(i,end='')
            print_counter += 1
# def print_ascii(fn):
#     f = open(fn,'r')
#     print(''.join([g for g in f]))


def game_start():
    time.sleep(1)
    print('-'*100)
    print('Welcome to Project 1')
    print('-'*100)
    print_ascii('ascii_front_page2.txt')
    time.sleep(1)
    print('This project will demonstrate the use of classes and interactions between instances')
    print('-'*100)

def hero_start():
    hero1 = Hero()
    time.sleep(1)
    hero1.show_data()
    hero1.set_current_hp(int(hero1.con * 25))
    return hero1

game_start()
hero1 = hero_start()
map1 = map_initialize()
lineup_list = monster_line_up()
map1.index_mapping(lineup_list)

while True:
    map1.print_map()
    map1.show_h_coordinate()
    map1.movement()
    monster_index = map1.monster_check()
    if type(monster_index) == int:
        print(hero1.return_name(), end='')
        print(' have encountered ', end ='')
        lineup_list[monster_index].print_name()
        A = battle_choice()
        if A == True:
            Battle(hero1,lineup_list[monster_index])
        elif A == False:
            if hero1.luc > lineup_list[monster_index].luc:
                time.sleep(1)
                print('you have successfully ran like a bitch')
                print('-'*50)
                time.sleep(1)
            else:
                Battle(hero1, lineup_list[monster_index])
    else:
        pass