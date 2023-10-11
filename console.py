#!/usr/bin/env python3
"""Console is a command interpreter for hbnb project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class containing all the interpreter command"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit    -   exit the program"""
        return True

    def do_EOF(self, line):
        """EOF    -   Ctrl-d handler"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
