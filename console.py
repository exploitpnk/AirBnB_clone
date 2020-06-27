#!/usr/bin/python3
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()