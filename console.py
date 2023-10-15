#!/usr/bin/env python3
"""Console is a command interpreter for hbnb project"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """Class containing all the interpreter command"""

    prompt = "(hbnb) "
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

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
        elif line not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        else:
            obj_Stg = HBNBCommand.__classes[line]()
            obj_Stg.save()
            print(obj_Stg.id)

    def do_show(self, line):
        '''Usage: 1. show <class name> <id> | 2. <class name>.show(<id>)
        Function: Shows the instance details of the class
        '''
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ')
            if args[0] not in HBNBCommand.__classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
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
            args = line.split(' ')
            if args[0] not in HBNBCommand.__classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
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
            args = line.split(' ')
            if args[0] not in HBNBCommand.__classes.keys():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == args[0]]
                print(obj_list)
        else:
            obj_list = [str(obj) for key, obj in storage.all().items()]
            print(obj_list)

    def do_update(self, line):
        """
        Usage: 1. update <class name> <id> <attribute name> "<attribute value>"
        Functionality: Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            args = line.split(' ', 3)
            if args[0] not in HBNBCommand.__classes.keys():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif "{}.{}".format(args[0], args[1]) not in storage.all():
                print("** no instance found **")
            else:
                key = "{}.{}".format(args[0], args[1])
                setattr(storage.all()[key], args[2], args[3])
                storage.save()

    def do_count(self, line):
        """
        Returns the count of instances of a particular class
        """
        if line != "":
            args = line.split(' ')
            if args[0] not in HBNBCommand.__classes.keys():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == args[0]]
                print(len(obj_list))
        else:
            obj_list = [str(obj) for key, obj in storage.all().items()]
            print(len(obj_list))

    def do_BaseModel(self, line):
        """
        Usage: BaseModel.<command>(<arguments>, ...)
        Functionality: call method on classes in another way
        """
        if line == "" or line is None:
            print("** command name missing **")
        else:
            _, command = line.split(".", 1)
            command = re.sub(r"[(),]", " ", command)
            args = command.split()
            if hasattr(self, f"do_{args[0]}"):
                getattr(self, f"do_{args[0]}")("BaseModel")
            else:
                print("** command doesn't exist **")

    def do_User(self, line):
        """
        Usage: User.<command>(<arguments>, ...)
        Functionality: call method on classes in another way
        """
        if line == "" or line is None:
            print("** command name missing **")
        else:
            _, command = line.split(".", 1)
            command = re.sub(r"[(),]", " ", command)
            args = command.split()
            if hasattr(self, f"do_{args[0]}"):
                getattr(self, f"do_{args[0]}")("User")
            else:
                print("** command doesn't exist **")

    def do_State(self, line):
        """
        Usage: State.<command>(<arguments>, ...)
        Functionality: call method on classes in another way
        """
        if line == "" or line is None:
            print("** command name missing **")
        else:
            _, command = line.split(".", 1)
            command = re.sub(r"[(),]", " ", command)
            args = command.split()
            if hasattr(self, f"do_{args[0]}"):
                getattr(self, f"do_{args[0]}")("State")
            else:
                print("** command doesn't exist **")

    def do_City(self, line):
        """
        Usage: City.<command>(<arguments>, ...)
        Functionality: call method on classes in another way
        """
        if line == "" or line is None:
            print("** command name missing **")
        else:
            _, command = line.split(".", 1)
            command = re.sub(r"[(),]", " ", command)
            args = command.split()
            if hasattr(self, f"do_{args[0]}"):
                getattr(self, f"do_{args[0]}")("City")
            else:
                print("** command doesn't exist **")

    def do_Amenity(self, line):
        """
        Usage: Amenity.<command>(<arguments>, ...)
        Functionality: call method on classes in another way
        """
        if line == "" or line is None:
            print("** command name missing **")
        else:
            _, command = line.split(".", 1)
            command = re.sub(r"[(),]", " ", command)
            args = command.split()
            if hasattr(self, f"do_{args[0]}"):
                getattr(self, f"do_{args[0]}")("Amenity")
            else:
                print("** command doesn't exist **")

    def do_Place(self, line):
        """
        Usage: Place.<command>(<arguments>, ...)
        Functionality: call method on classes in another way
        """
        if line == "" or line is None:
            print("** command name missing **")
        else:
            _, command = line.split(".", 1)
            command = re.sub(r"[(),]", " ", command)
            args = command.split()
            if hasattr(self, f"do_{args[0]}"):
                getattr(self, f"do_{args[0]}")("Place")
            else:
                print("** command doesn't exist **")

    def do_Review(self, line):
        """
        Usage: Review.<command>(<arguments>, ...)
        Functionality: call method on classes in another way
        """
        if line == "" or line is None:
            print("** command name missing **")
        else:
            _, command = line.split(".", 1)
            command = re.sub(r"[(),]", " ", command)
            args = command.split()
            if hasattr(self, f"do_{args[0]}"):
                getattr(self, f"do_{args[0]}")("Review")
            else:
                print("** command doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
