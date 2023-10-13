#!/usr/bin/python3
"""Console module for AirBnB Clone Project"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exits the command interpreter"""
        return True

    def do_EOF(self, args):
        """Handles end of file (EOF)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line + ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, save it, and prints its id"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.models:
            print("** class doesn't exist **")
        else:
            new_instance = storage.models[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(objects[obj]) for obj in objects])
        elif args[0] not in storage.models:
            print("** class doesn't exist **")
        else:
            print([str(objects[obj]) for obj in objects if obj.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.models:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
