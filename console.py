#!/usr/bin/python3
"""
Defines a program called console.py that contains the entry point of the
command interpreter
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""Defines the imported modules"""


class HBNBCommand(cmd.Cmd):
    """Defines the class HBNBCommand that inherits from cmd.Cmd."""
    prompt = "(hbnb) "

    def emptyline(self):
        """When no command is entered, do nothing"""
        pass

    def do_quit(self, arg):
        """Gracefully quits the program"""
        return True

    def do_EOF(self, arg):
        """Triggers an EOF (End of File) interrupt to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id.
        """
        args = arg.split()
        if arg:
            pass
        else:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity",
                           "Place", "Review"]:
            print("** class doesn't exist **")
            return
        else:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based (or not) on the
        class name.
        """
        objs = []
        if arg in ["BaseModel"] or len(arg) == 0:
            for obj in storage.all().values():
                objs.append(str(obj))
            print(objs)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        """
        Updates an instance
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) < 1:
            print('** class name missing **')
            return
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"]:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], eval(args[3]))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
