#!/usr/bin/python3
"""module for class HBNBCommand"""


import cmd
import os
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class to contain entry point of the command interpreter"""

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
