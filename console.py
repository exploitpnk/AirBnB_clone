#!/usr/bin/python3
""" Console - Simple command interpreter for Airbnb"""
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
        """ Creates a new instance """
        if not arg:
            print('** class name missing **')
            return None
        try:
            model = eval(arg + "()")
            model.save()
            print(model.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Show instance dictorinary based in ID """
        argv = arg.split()
        if not argv:
            print("** class name missing **")
            return None
        try:
            eval(argv[0])
        except:
            print("** class doesn't exist **")
            return None

        objects = storage.all()

        if len(argv) < 2:
            print("** instance id missing **")
            return None
        argv[1] = argv[1].replace("\"", "")
        key = argv[0] + '.' + argv[1]

        if objects.get(key, False):
            print(objects[key])
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        argv = arg.split()
        if not argv:
            print('** class name missing **')
            return None
        try:
            eval(argv[0])
        except:
            print("** class doesn't exist **")
            return None

        objects = storage.all()

        if len(argv) < 2:
            print("** instance id missing **")
            return None

        argv[1] = argv[1].replace("\"", "")
        key = argv[0] + '.' + argv[1]

        if objects.get(key, False):
            objects.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        args = arg.split()

        if len(args) != 0:
            if args[0] == "BaseModel":
                if len(args) == 1:
                    print('** instance id missing **')
                else:
                    key = args[0] + '.' + args[1]
                    if key in storage.all():
                        if len(args) > 2:
                            if len(args) <= 3:
                                print('** value missing **')
                            else:
                                setattr(
                                    storage.all()[key],
                                    args[2],
                                    args[3][1:-1])
                                storage.all()[key].save()
                        else:
                            print('** attribute name missing **')
                    else:
                        print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
