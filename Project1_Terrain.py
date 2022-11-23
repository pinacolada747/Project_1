import random
import time

def occupant_check(location,location_list):
    if location in location_list:
        return True
    else:
        return False

class location():
    def set_data(self, *data):
        self.y_value = data[0]
        self.x_value = data[1]
        self.symbol = data[2]
        self.h_here = data[3]
    def show_data(self):
        if self.h_here == '1':
            print('H',end = '')
            print(' | ', end='')
        else:
            print(self.symbol, end = '')
            print(' | ', end = '')

    def set_h_here(self,parameter):
        self.h_here = parameter

    def return_symbol(self):
        return self.symbol

    def return_y_value(self):
        return self.y_value
    def return_x_value(self):
        return self.x_value

# things to address
# pathing issue
# 1. create two spaces in random directions surrounding all objects
# 2. generate a pathway towards entry to be blank
# 3. The wolverine - movement (miniboss)

class Map():

    def __init__(self):
    #Monster location and portal generation
        in_out_list = []
        monster_locations = []
        bd_list = [0, 9]
        a = random.randint(0, 9)
        b = random.choice(bd_list)
        c = random.choice(bd_list)
        d = random.randint(0, 9)
        in_out_list.append([a, b])
        in_out_list.append([c, d])
        for k in range(5):
            e = random.randint(0, 9)
            f = random.randint(0, 9)
            while occupant_check([e, f], in_out_list + monster_locations):
                e = random.randint(0, 9)
                f = random.randint(0, 9)
            monster_locations.append([e, f])
        self.monster_locations = monster_locations
        self.in_out_list = in_out_list

    #Actual map list of list Generation
        terrain_list = []
        for y in range(0,10):
            terrain_list.append([])
            for x in range(0,10):
                location1 = location()
                if [y, x] == self.in_out_list[0]:
                    location1.set_data(y, x, 'I','1')
                    self.set_h_coordinate(y,x)
                elif [y, x] == self.in_out_list[1]:
                    location1.set_data(y, x, 'O','0')
                elif [y, x] in self.monster_locations:
                    location1.set_data(y, x, 'M','0')
                else:
                    obstacle_chance = random.randint(0,100)
                    if obstacle_chance < 65:
                        location1.set_data(y, x, ' ','0')
                    else:
                        location1.set_data(y, x, '#','0')
                terrain_list[y].append(location1)
                self.map = terrain_list

    #Monster location map to monster list

    def index_mapping(self,monster_line_up):
        for m in range(len(monster_line_up)):
            y = self.return_monster_y_coordinate(m)
            x = self.return_monster_x_coordinate(m)
            monster_line_up[m].set_coordinate(y,x)
        for m2 in range(len(monster_line_up)):
            print('Monster', m2 + 1, 'is located at YX:',end ='')
            monster_line_up[m2].show_coordinates()

    def return_monster_y_coordinate(self,monster_index):
        return self.monster_locations[monster_index][0]

    def return_monster_x_coordinate(self,monster_index):
        return self.monster_locations[monster_index][1]

    def monster_check(self):
        for m3 in range(len(self.monster_locations)):
            if [self.h_y_value,self.h_x_value] == [self.monster_locations[m3][0],self.monster_locations[m3][1]]:
                return m3
            else:
                pass

    # def self.h_y_value
    # if self.h_y_value self.h_x_value -
    # monster line up (list of class)
    # battle(monster_line_up)
    #     for in range
    #     monster_list[0].return_x_value()

    def set_h_coordinate(self,*data):
        self.h_y_value = data[0]
        self.h_x_value = data[1]

    def show_h_coordinate(self):
        print('Y:',self.h_y_value,'X:',self.h_x_value)

    def print_map(self):
        for y in range(len(self.map)):
            print('')
            print('-'*41)
            print('| ',end ='')
            for x in range(len(self.map)):
                if [self.h_y_value,self.h_x_value] == [self.map[y][x].return_y_value(),self.map[y][x].return_x_value()]:
                    self.map[y][x].set_h_here('1')
                    self.map[y][x].show_data()
                    self.map[y][x].set_h_here('0') #is this the best method?
                else:
                    self.map[y][x].show_data()

        print('')
        print('-'*41)

    def terrain_check(self,direction):
        if direction == 'w':
            if self.map[((lambda y: y - 1)(self.h_y_value))][self.h_x_value].return_symbol() != '#':
                return True
        elif direction == 's':
            if self.map[int((lambda y: y + 1)(self.h_y_value))][self.h_x_value].return_symbol() != '#':
                return True
        elif direction == 'd':
            if self.map[self.h_y_value][int((lambda x: x + 1)(self.h_x_value))].return_symbol() != '#':
                return True
        elif direction == 'a':
            if self.map[self.h_y_value][int((lambda x: x - 1)(self.h_x_value))].return_symbol() != '#':
                return True

    # def monster_check(self):
    #     if self.map[self.h_y_value][self.h_x_value].return_symbol() == 'M':
    #         return True

    def movement(self):
        movement = input('W for North, S for South, D for East, A for West: ')
        if movement == 'w':
            if self.h_y_value > 0 and self.terrain_check('w') == True:
                self.h_y_value -= 1
            else:
                print('you have hit a wall')
                pass
        elif movement == 's':
            if self.h_y_value < 9 and self.terrain_check('s') == True:
                self.h_y_value += 1
            else:
                print('you have hit a wall')
                pass
        elif movement == 'd':
            if self.h_x_value < 9 and self.terrain_check('d') == True:
                self.h_x_value += 1
            else:
                print('you have hit a wall')
        elif movement == 'a':
            if self.h_x_value > 0 and self.terrain_check('a') == True:
                self.h_x_value -= 1
            else:
                print('you have hit a wall')
        else:
            pass

# map_list = []
# for i in range(4):
#     map1 = Map()
#     map_list.append(map1)
#
# for j in range(len(map_list)):
#     map_list[j].print_map()

def map_initialize():
    map1 = Map()
    time.sleep(1)
    return map1

def main():
    map1 = map_initialize()
    while True:
        map1.movement()
        map1.print_map()
        map1.show_h_coordinate()
        map1.monster_check()


    # monster_allocation()

if __name__ == '__main__':
    main()

    # terrain_types = obstacle, land, entry, exit
    # y, x value = 0 to 9
    # explored = true false
    # drops = potion, side arm

# class MyClass:
#     def __init__(self, name):
#         self.name = name
#         self.pretty_print_name()
#
#     def pretty_print_name(self):
#         print("This object's name is {}.".format(self.name))
#
# my_objects = {}
# for i in range(1,11):
#     name = 'obj_{}'.format(i)
#     my_objects[name] = my_objects.get(name, MyClass(name = name))
#


