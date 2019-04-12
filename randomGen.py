#!/bin/python3
import random


def printtable(map):
    for y in range(len(map)):
        line = ''
        for x in range(len(map[y])):
            if map[y][x] != 0:
                line += str(map[y][x])
            else:
                line += ' '
            line += ' '
        print(line)
    print('---------')


def generateMap(modules, dimension):
    map = [[0 for x in range(dimension)] for y in range(dimension)]

    i = 0
    while i < len(modules):
        if i == 0:
            y = random.randint(1, len(map) - 1)
            x = random.randint(0, len(map[y]) - 1)

            map[y][x] = 1

            # print(str(y) + ' ' + str(x))

            i += 1
            # printtable(map)
            continue

        while True:
            while True:
                y = random.randint(0, len(map) - 1)
                x = random.randint(0, len(map[y]) - 1)

                if map[y][x] != 0:
                    break

            if map[y][x] == 1:
                available = [0, 0, -1, 0]
            else:
                available = [0, 0, 0, 0]

            if available[0] == 0 and y > 0 and map[y - 1][x] == 0:
                available[0] = 1

            if available[1] == 0 and x < 4 and map[y][x + 1] == 0:
                available[1] = 1

            if available[2] == 0 and y < 4 and map[y + 1][x] == 0:
                available[2] = 1

            if available[3] == 0 and x > 0 and map[y][x - 1] == 0:
                available[3] = 1

            mod = -1

            if 1 in available:
                # if available.count(1) >= 2:
                # print(available.count(1));
                break

        while True:
            mod = random.randint(0, 3)
            if available[mod] == 1:
                break

        if mod == 0:
            y -= 1
        elif mod == 1:
            x += 1
        elif mod == 2:
            y += 1
        elif mod == 3:
            x -= 1

        '''if i == 9 and 2 not in map:
            map[y][x] = 2
        elif i == 8 and 3 not in map:
            map[y][x] = 3
        else:
            map[y][x] = random.randint(4, len(modules))'''

        map[y][x] = i + 1;

        # printtable(map)

        i += 1

    printtable(map)

    rooms = {}

    for y in range(len(map)):
        line = ''
        for x in range(len(map[y])):
            if (map[y][x] == 0):
                continue

            room = {}

            if y > 0 and map[y - 1][x] != 0:
                room.update({'north': modules[map[y - 1][x] - 1]})
            if x < len(map[y]) - 1 and map[y][x + 1] != 0:
                room.update({'east': modules[map[y][x + 1] - 1]})
            if y < len(map) - 1 and map[y + 1][x] != 0:
                room.update({'south': modules[map[y + 1][x] - 1]})
            if x > 0 and map[y][x - 1] != 0:
                room.update({'west': modules[map[y][x - 1] - 1]})

            #print(str(room))
            rooms.update({modules[map[y][x] - 1]: room})
            #print(str(rooms))

    items = {
        0: 'portion',
        1: 'key',
        2: 'monster'
    }

    i = 0;
    while i < 3:
        room = random.choice(list(rooms.keys()))

        if 'item' in rooms[room] or room == 'Hall' or room == 'Garden':
            continue

        rooms[room].update({'item': items[i]})

        i += 1

    return rooms, map;
