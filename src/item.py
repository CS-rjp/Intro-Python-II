# Implement a class to item information. This should have name and
# description attributes.

"""
    Thoughts to manage building items:
    If a player is carrying an item it should appear in all rooms unless a player sets it down and leaves it.
    There are specific rooms with items that do not appear anywhere else (treasure) or items that a Player must find
    and choose to aid them in tasks later.    
"""

class Item:
    """
    every item has a name and description
    """

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
        #self.location = location # sectors of the room
        #self.room = room  # we should already have this information from class Room(self.name)

    def __str__(self):
        return f'There is a {self.descr} {self.name}'#' {self.location}'#' in the {self.room}. '

    
