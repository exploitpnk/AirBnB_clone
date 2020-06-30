#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
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

    def do_show(self, arg):
        """ Print instances from id """
        argv = arg.split()
        if not argv:
            print("** class name missing **")
            return None
        try:
            eval(argv[0])
        except:
            print("** class doesn't exist **")
            return None

        al = storage.all()

        if len(argv) < 2:
            print("** instance id missing **")
            return None
        argv[1] = argv[1].replace("\"", "")
        key = argv[0] + '.' + argv[1]

        if al.get(key, False):
            print(al[key])
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
