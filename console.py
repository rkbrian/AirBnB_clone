#!/usr/bin/python3
"""module for class HBNBCommand"""


import cmd
import os
import json
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """class to contain entry point of the command interpreter"""

    classname = {"BaseModel": BaseModel, "User": User, "Place": Place,
                 "State": State, "City": City, "Amenity": Amenity,
                 "Review": Review}
    prompt = '(hbnb) '

    def emptyline(self):
        """press enter does nothing"""
        pass

    def help_quit(self):
        """command for (help quit)"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """command for (help EOF)"""
        print("EOF command to exit the program\n")

    def do_quit(self, arg):
        """command to exit interface"""
        return True

    def do_EOF(self, arg):
        """command to exit interface"""
        return True

    def do_create(self, arg):
        """create new instance of BaseModel, save it and print id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg in self.classname.keys():
            for keys, values in self.classname.items():
                if arg == keys:
                    tempval = values()
                    tempval.save()
                    print(tempval.id)
                    break
        else:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """print str rep of an inst based on class name and id"""
        larg = arg.split()
        if len(larg) == 0:
            print("** class name missing **")
            return
        elif larg[0] not in self.classname.keys():
            print("** class doesn't exist **")
            return
        elif len(larg) == 1:
            print("** instance id missing **")
            return
        elif len(larg) == 2:
            temp_val = larg[0] + "." + larg[1]
            if temp_val in models.storage.all().keys():
                print(models.storage.all()[temp_val])
            else:
                print("** no instance found **")
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """delete an instance based on class name and id"""
        larg = arg.split()
        if len(larg) == 0:
            print("** class name missing **")
            return
        elif larg[0] not in self.classname.keys():
            print("** class doesn't exist **")
            return
        elif len(larg) == 1:
            print("** instance id missing **")
            return
        elif len(larg) == 2:
            temp_val = larg[0] + "." + larg[1]
            if temp_val in models.storage.all().keys():
                del models.storage.all()[temp_val]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** no instance found **")
            return

    def do_all(self, arg=None):
        """prints all string representation of all instances"""
        listr = []
        if not arg:
            for keys in models.storage.all().keys():
                listr.append(str(models.storage.all()[keys]))
            print(listr)
        elif arg in self.classname.keys():
            for keys, values in models.storage.all().items():
                if arg in keys:
                    listr.append(str(values))
            print(listr)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        """update an instance based on class name and id"""
        larg = arg.split()
        if len(larg) == 0:
            print("** class name missing **")
            return
        elif larg[0] not in self.classname.keys():
            print("** class doesn't exist **")
            return
        elif len(larg) == 1:
            print("** instance id missing **")
            return
        for keys in models.storage.all().keys():
            if larg[0] + "." + larg[1] == keys:
                break
        else:
            print("** no instance found **")
            return
        if len(larg) == 2:
            print("** attribute name missing **")
            return
        elif len(larg) == 3:
            print("** value missing **")
            return
        else:
            for keys, values in models.storage.all().items():
                if larg[0] + "." + larg[1] == keys:
                    if larg[2] in values.__dict__.keys():
                        attr = getattr(values, larg[2])
                        setattr(values, larg[2], type(attr)(larg[3][1: -1]))
                    else:
                        setattr(values, larg[2], (larg[3][1: -1]))
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
