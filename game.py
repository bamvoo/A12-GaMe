#!/bin/python3
def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
  
  w + ENTER --> north
  d + ENTER --> east
  s + ENTER --> south
  a + ENTER --> weast

  SPACE + ENTER --> get item

''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print("Inventory : " + str(inventory))
    print("Directions : " + str(directions))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('''---------------------------
        ''')

# array with directions to go in the moment
directions = {'north','east','south','west'}
# an inventory, which is initially empty
inventory = []
# a dictionary linking a room to other room positions
rooms = {
    'Hall': {'south': 'Kitchen',
             'east': 'Dining Room',
             'item': 'key'
             },
    'Kitchen': {'north': 'Hall',
                'item': 'monster'
                },

    'Dining Room': {'west': 'Hall',
                    'south': 'Garden',
                    'item': 'potion'
                    },

    'Garden': {'north': 'Dining Room'}
}
# start the player in the Hall
currentRoom = 'Hall'
showInstructions()
# loop forever
while True:
    showStatus()
    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    
    move = move.lower()
    # if they type 'go' first

    if move == 'w':
        move = 'go north'
        move = move.split()
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
                # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    elif move == 'd':
        move = 'go east'
        move = move.split()
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
                # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    elif move == 's':
        move = 'go south'
        move = move.split()
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
                # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    elif move == 'a':
        move = 'go west'
        move = move.split()
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
                # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    elif move == " ":
        # if the room contains an item, and the item is the one they want to get
        if 'item' in rooms[currentRoom]:
            # add the item to their inventory
            inventory += [rooms[currentRoom]['item']]
            # display a helpful message
            print(rooms[currentRoom]['item'] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get!')
    

    # player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        if 'potion' in inventory:
            print('You throw the potion to the beast and u defeat them.')
            inventory.remove('potion')
            rooms[currentRoom].pop('item')
            # Eliminar posiocion monster y potion de los arrays.
        else :  
            print('A monster has got you... GAME OVER!')
            break
            
            
    # player wins if they get to the garden with a key and a shield
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
