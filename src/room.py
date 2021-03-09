# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room, descr): # , room, attribute):
        self.room = room
        self.descr = descr

    def __str__(self):
        return (f'You are in the {self.room} room. {self.descr} ')
