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

    def do_all(self, line):
        """Printsallstring representationofallinstancesbased on/nor class name
        """
        liste = []
        dic_temp = models.storage.all()
        for i in dic_temp.values():
            liste.append(str(i))
        if line:
            if line not in globals():
                print("** class doesn't exist **")
            else:
                print(liste)
        else:
            print(liste)

    def do_EOF(self, arg):
        """ Exit the program """
        print()
        return True

    def emptyline(self):
        """Handles the emptylines"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
