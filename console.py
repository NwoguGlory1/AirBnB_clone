#!/usr/bin/python3
"""
Defines a program called console.py that contains the entry point of the 
command interpreter
"""


import cmd
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
            Ex: $ create BaseModel

        If the class name is missing, prints ** class name missing ** 
            Ex: $ create

        If the class name doesn’t exist, print ** class doesn't exist **
            Ex: $ create MyModel
        """
        if arg == "BaseModel":
            BaseModel()
        elif arg == "" or arg == None:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name
        and id.
            Ex: $ show BaseModel 1234-1234-1234.

        If the class name is missing, prints ** class name missing **
            Ex: $ show

        If the class name doesn’t exist, prints ** class doesn't exist **
            Ex: $ show MyModel

        If the id is missing, prints ** instance id missing **
            Ex: $ show BaseModel

        If the instance of the class name doesn’t exist for the id, prints
        ** no instance found **
            Ex: $ show BaseModel 121212
        """

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234

        If the class name is missing, prints ** class name missing **
            Ex: $ destroy

        If the class name doesn’t exist, prints ** class doesn't exist **
            Ex:$ destroy MyModel

        If the id is missing, prints ** instance id missing **
            Ex: $ destroy BaseModel

        If the instance of the class name doesn’t exist for the id, prints
        ** no instance found **
            Ex: $ destroy BaseModel 121212
        """

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
            Ex: $ all BaseModel or $ all

        The printed result is a list of strings
        If the class name doesn’t exist, prints ** class doesn't exist **
            Ex: $ all MyModel
        """

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (saves the change into the JSON file)
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Only one attribute can be updated at the time
        """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
