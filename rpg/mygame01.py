#!/usr/bin/env python3

# Replace RPG starter project with this code when new instructions are live

from rooms import rooms

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom + '.')
  if "desc" in rooms[currentRoom]:
    print(rooms[currentRoom]['desc'])

  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('\nYou see a ' + rooms[currentRoom]['item'] + '!')

  print('\n')

  for key in rooms[currentRoom]['direction']:
      print('-To the {0} you see the {1}'.format(key, rooms[currentRoom]['direction'][key]))

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]['direction']:
      #set the current room to the new room
      currentRoom = rooms[currentRoom]['direction'][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  if move[0] == 'inventory' :
    #print the current inventory
    print('Inventory : ' + str(inventory))

  if move[0] == 'exit' :
    #print the current inventory
    print('Goodbye!')
    break

  if move[0] == 'teleport':
    if move[1] in rooms.keys():
      print('Teleporting to {0}!'.format(move[1]))
      currentRoom = move[1]
    else:
        print('You can\'t teleport to {0}!'.format(move[1]))

  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
      print("A monster has got you!... GAME OVER!")
      break

  # define how a player can win
  if currentRoom == 'Balcony' and 'pizza' in inventory and 'beer' in inventory:
      print('You\'ve successfully ignored all your problems and will instead have pizza and beer on the balcony, overlooking an impressive natural vista!')
      break
