#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import *


class HBNBCommand(cmd.Cmd):
    """The command interpreter class for the AirBnB clone project"""
    prompt = "(hbnb) "

    def do_create(self, line):
        """ Create an item """
        if not line:
            print("Class name missing")
            return

        clss = line.split()[0]
        if clss in globals():
            var = globals()[clss]
            print(var)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Print str representation of an instance based on cls name & id"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """ Exit the program """
        print()
        return True

    def emptyline(self):
        """Handles the emptylines"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
