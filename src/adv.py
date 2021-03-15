from player import Player
from room import Room
from item import Item


# Declare all the rooms
room_outside = Room("Forest Outside the Cave Entrance",
                     "North of you, the cave mount beckons."),

room_foyer = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

room_overlook = Room("Grand Overlook", """A steep cliff appears before you, falling.
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

room_narrow = Room("Narrow Passage", """The narrow passage bends here from west.
to north. The smell of gold permeates the air."""),

room_treasure = Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# create an instance of game class
my_game = Game("Adventure Game", [room_outside, room_foyer, room_narrow, room_overlook, room_treasure])

# create a variable to hold users choice
room_choice = []
while choice != len(my_game.rooms) + 1:
  # print out the menu
  print (my_game)

  # request input from user
  room_choice = input("Select the room you wish to enter by stating the direction you wish to go (N, S, E, or W): ")
  # use conditionals to identify an appropriate selection is made (NSEW)
  # if room_choice = 'N' ...
  # elif room_choice = 'S' ...
  # elif room_choice = 'E' ...
  # elif room_choice = 'W' ...
  # else:
  #   print (f'Please enter N, S, E, or W only. ')
  #   continue

# print the user selection/choice
print(f'my_game.rooms(choice)')


# Main
#
class Game:
  def __init__(self, name="Adventure Game!", rooms=[]):
    self.name = name
    self.rooms = rooms

  def adventure_game():
    print (f'Welcome to the Adventure Game!')

    # Make a new player object that is currently in the 'outside' room.
    player_1 = input(str("What is your name? (limit 16 characters) "))
    #print(f'Hello, {player_1}!  It is nice to meet you. ')

    # Write a loop that:
    #
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.


if __name__ == '__main__':
  adventure_game()