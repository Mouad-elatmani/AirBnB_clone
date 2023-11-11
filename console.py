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
        """Prints the string representation of an instance based \
                on the class name and id
        """
        if line:
            liste = line.split()
            if len(liste) == 0:
                print("** class name missing **")
            elif liste[0] not in globals():
                print("** class doesn't exist **")
            elif len(liste) == 1:
                print("** instance id missing **")
            else:
                dict_temp = models.storage.all()
                key = f"{liste[0]}.{liste[1]}"
                if key in dict_temp:
                    print(dict_temp[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return True

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line:
            liste = line.split()
            if liste[0] not in globals():
                print("** class doesn't exist **")
            elif len(liste) == 1:
                print("** instance id missing **")
            else:
                dict_temp = models.storage.all()
                key = f"{liste[0]}.{liste[1]}"
                if key in dict_temp:
                    del dict_temp[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print('** class name missing **')

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
