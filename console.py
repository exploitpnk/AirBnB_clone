#!/usr/bin/python3
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """ Simple command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Ctrl+D to exit the programm """
        return True

    def emptyline(self):
        """ Empty line """
        pass


    def do_create(self, arg):
        """ Creates a new instance of (arg) """
        if not arg:
            print("** class name missing **")
            return None
        try:
            mo = eval(arg + "()")
            mo.save()
            print(mo.id)
        except:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
