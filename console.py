#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    do_EOF = do_quit

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
