# Implement a class to hold room information. This should have name and
# description attributes.

from item import Items

class Room:
    def __init__(self, name, descr): # , room, attribute):
        """
        the adventure game has_many rooms
        """
        self.name = name
        self.descr = descr

    def __str__(self):
        output = f'\t{self.name}'

        return (f'You are in the {self.name} room. {self.descr} ')

        if len(self.items) < 1:
            return f'There are no items found in {self.name}'

        for item in self.items:
            output += f'{product}\n'

        return output