#!/usr/bin/python3
"""module for class HBNBCommand"""


import cmd
import os
import json
import models
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """class to contain entry point of the command interpreter"""

    classname = ["BaseModel", "User"]

    def __init__(self):
        """class initialization"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def emptyline(self):
        """press enter does nothing"""
        pass

    def help(self):
        """command for help"""
        print("\nDocumented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit\n")

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
        if not arg:
            print("** class name missing **")
        for key, value in models.storage._FileStorage__objects[key]:
            if arg == key:
                tempval = value
                tempval.save()
        if tempval.id:
            print(tempval.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """print str rep of an inst based on class name and id"""
        larg = arg.split()
        if len(larg) == 0:
            print("** class name missing **")
        elif larg[0] not in self.classname:
            print("** class doesn't exist **")
        elif len(larg) == 1:
            print("** instance id missing **")
        elif len(larg) == 2:
            for keys, values in models.storage._FileStorage__objects[keys]:
                if larg[0] + "." + larg[1] == keys:
                    print(values)
            else:
                print("** instance id missing **")

    def do_destroy(self):
        """delete an instance based on class name and id"""
        larg = arg.split()
        if len(larg) == 0:
            print("** class name missing **")
        elif larg[0] not in self.classname:
            print("** class doesn't exist **")
        elif len(larg) == 1:
            print("** instance id missing **")
        elif len(larg) == 2:
            for keys, values in models.storage._FileStorage__objects[keys]:
                if larg[0] + "." + larg[1] == keys:
                    del models.storage._FileStorage__objects[keys]
                    models.storage.save
            else:
                print("** instance id missing **")

    def do_all(self, arg=None):
        """prints all string representation of all instances"""
        if arg in self.classname:
            listr = []
            for keys, values in models.storage._FileStorage__objects[keys]:
                if arg in keys:
                    listr.append(str(values))
            print(listr)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update an instance based on class name and id"""
        larg = arg.split()
        if len(larg) == 0:
            print("** class name missing **")
            return
        elif larg[0] not in self.classname:
            print("** class doesn't exist **")
            return
        elif len(larg) == 1:
            print("** instance id missing **")
            return
        elif len(larg) == 2:
            print("** attribute name missing **")
            return
        elif len(larg) == 3:
            print("** value missing **")
            return
        else:
            #halfn = len(larg) / 2
            for keys, values in models.storage._FileStorage__objects[keys]:
                #for i in range(1, halfn):
                    #if larg[i * 2] + "." + larg[i * 2 + 1] == keys:
                if larg[2] + "." + larg[3] == keys:
                    attr = getattr(keys, larg[2])
                    if isinstance(attr, (str or int or float)):
                        setattr(keys, larg[2], isinstance(attr))
            models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
