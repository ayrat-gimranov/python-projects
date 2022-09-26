# test
#!/usr/bin/python3
"""Ghost Busters - a game adapted from Alta3 lab"""

from genericpath import exists
from string import capwords


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    Ghostbusters! Catch 6 ghosts.
    Shoot to catch the ghost with a proton pack. Then find a way back to HQ to dump the proton pack into a containment unit.
    ========
    Commands:
      go [direction]
      shoot [ghost name]
      dump

    Instructions:
      help
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentLocation)
    # print the contents of a proton pump
    print('Proton Pack:', proton_pack)
    # check if there's a ghost in the room, if so print it
    if "ghost" in locations[currentLocation]:
      print('You found a ghost! - ' + locations[currentLocation]['ghost'])
    if 'containment unit' in locations[currentLocation]:
      print('Ghosts imprisoned:', containment_unit)
      print(f'Ghosts on the run: {6 - len(containment_unit)}')
    print("---------------------------")

# a proton pack, used to catch a ghost, initially empty
# can contain one ghost at a time
proton_pack = []

# containment unit at HQ, initially empty, where proton pack needs to be dumped
containment_unit = []

# a dictionary linking a location to other locations
locations = {

            'HQ' : {
                  'north' : 'Columbia University',
                  'south' : 'Movie Theater',
                  'east'  : 'Library',
                  'containment unit' : containment_unit
                },

            'Restaurant' : {
                  'north' : 'City Hall',
                  'south' : 'Library',
                  'west'  : 'Courthouse',
                },
            'Courthouse' : {
                  'east' : 'Columbia University',
                  'ghost': 'Scoleri Brothers'
                },
            'Sedgewick Hotel' : {
                  'east' : 'Spook Central',
                  'ghost': 'Slimer'
                },
            'Spook Central' : {
                  'south': 'Museum',
                  'east' : 'Movie Theater',
                  'west' : 'Sedgewick Hotel'
            },
            'Library': {
                  'north': 'Restaurant',
                  'west' : 'HQ',
                  'ghost' : 'Library Ghost'
            },
            'Movie Theater': {
                  'north': 'HQ',
                  'west' : 'Spook Central',
                  'ghost': 'Movie Theater Ghost'
            },
            'Museum': {
                  'north': 'Spook Central',
                  'ghost': 'Gozer'
            },
            'City Hall': {
                  'south': 'Restaurant',
                  'ghost': 'Stay Puft'
            },
            'Columbia University': {
                  'south': 'HQ',
                  'east' : 'Restaurant',
                  'west' : 'Courthouse'
            }
         }

# start the player in the HQ
currentLocation = 'HQ'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "go east" becomes ["go", "east"]          
    move = move.lower().split(" ", 1)

    # provide instructions again if user asks for help
    if move[0] == 'help':
      showInstructions()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in locations[currentLocation]:
            #set the current room to the new room
            currentLocation = locations[currentLocation][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'shoot' first

    if move[0] == 'shoot' and len(move) > 1 and len(move[1]) > 0:
            
        # Capitalize the entered ghost name
        move[1] = capwords(move[1])        
        # make checks:
        # if the current location contains that ghost
        # if the ghost matches the ghost name the player wishes to catch
        # if proton pump already has a ghost in it

        if "ghost" in locations[currentLocation] and move[1] in locations[currentLocation]['ghost']:          
            if len(proton_pack) == 0:              
                # add the ghost into the proton pack
                proton_pack.append(move[1])
                #display a helpful message
                print(move[1] + ' is captured! Bring it to HQ and dump into Containing Unit.')
                #delete the item key:value pair from the room's dictionary
                del locations[currentLocation]['ghost']
            else:
                # let user know that proton pump is full
                print(f"Couldn't capture {move[1]}! Proton pump already has {proton_pack[0]} in it.")
                print("Return to HQ and dump the proton pack into Containing Unit.")
        # if there's no ghost in the location or the ghost name doesn't match
        else:
            #tell them they can't get it
            print(f"{move[1]} is not here!")
    
    # if the type dump first
    if move[0] == 'dump':
        # check that: 
        # 1 - containing room is present at the location
        # 2 - proton pack has a ghost in it
        if 'containment unit' in locations[currentLocation] and len(proton_pack) > 0:
            # add a ghost from proton pump to a containment unit
            containment_unit.append(proton_pack[0])
            proton_pack = []
            print("The ghost is successfully transferred to Containing Unit.")
        # if player is not at HQ
        else:
          print("Can't dump!")

    ## Define how a player can win
    if len(containment_unit) == 5:
        print('You caught all of the ghosts! VICTORY !!!')
        break