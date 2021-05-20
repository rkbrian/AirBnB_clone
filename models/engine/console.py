#!/usr/bin/python3
"""module for class HBNBCommand"""


import cmd
import os


class HBNBCommand(cmd.Cmd):
    """class to contain entry point of the command interpreter"""

    exit_str = ["EOF", "quit"]

    def __init__(self):
        """class initialization"""
        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb)"

    def help(self, *arg):
        """command for help"""
        if arg and len(arg):
            if arg[0] = "help":
                if arg[1] == exit_str[0]:
                    print("EOF command to exit the program")
                elif arg[1] == exit_str[1]:
                    print("Quit command to exit the program")
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit")

    def quit(self):
        """command to exit interface"""
        

    if __name__ == '__main__':
    HBNBCommand().cmdloop()
