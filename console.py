#!/usr/bin/env python3
"""Console is a command interpreter for hbnb project"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class containing all the interpreter command"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit    -   exit the program"""
        return True

    def do_EOF(self, line):
        """EOF    -   Ctrl-d handler"""
        return True

    def do_create(self, line):
        '''Usage: 1. create <class name> | 2. <class name>.create()
        Function: Creates an instance of the class
        '''
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj_Stg = storage.classes()[line]()
            obj_Stg.save()
            print(obj_Stg.id)

    def do_show(self, line):
        '''Usage: 1. show <class name> <id> | 2. <class name>.show(<id>)
        Function: Shows the instance details of the class
        '''
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])


    def do_destroy(self, line):
        '''Usage: 1. destroy <class name> <id> | 2. <class name>.delete(<id>)
        Function: Deletes the instance  of the class
        '''
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()


    def do_all(self, line):
        '''Usage: 1. all | 2. all <class name> | 3. <class name>.all()
        Function: Prints the string representation of all instances
        '''
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                strList = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(strList)
        else:
            new_strList = [str(obj) for key, obj in storage.all().items()]
            print(new_strList)


if __name__ == "__main__":
    HBNBCommand().cmdloop()