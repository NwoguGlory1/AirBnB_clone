#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """ prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = None
        if len(args) > 1:
            instance_id = args[1]

            try:
                instance = storage.get(class_name, instance_id)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")
 
    def do_destroy(self, arg):
        """deletes an instance based on the class name and id (save change into JSON file)"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = None
        if len(args) > 1:
            instance_id = args[1]

        try:
            instance = storage.get(class_name, instance_id)
            if instance:
                storage.delete(instance)
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """prints all string representation of all instances based or not on the class name"""
        if not arg:
            instances = storage.all()
        else:
            try:
                instances = storage.all(eval(arg))
            except NameError:
                print("** class doesn't exist **")
                return

            print([str(instance) for instance in instances.values()])

    def do_update(self, arg):
        """updates an instance based on the class name and id by adding or updating attribute (save change into JSON file) """
        if not arg:
            print("** class name missing **")
            return

        args = [a.strip('"') for a in arg.split(' ', 3)]
        if len(args) < 1:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = None
        if len(args) > 1:
            instance_id = args[1]

        try:
            instance = storage.get(class_name, instance_id)
            if instance:
                if len(args) > 2:
                    attribute_name = args[2]
                else:
                    print("** attribute name missing **")
                    return

                if len(args) > 3:
                    attribute_value = args[3]
                else:
                    print("** value missing **")
                    return

                setattr(instance, attribute_name, attribute_value)
                instance.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
