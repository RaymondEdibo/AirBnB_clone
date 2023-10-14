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

    def count(self, arg):
        """
        Prints number of instances
            usage: count <class_name>
        """
        args = shlex.split(arg)
        models.storage.reload()
        if len(args) < 1:
            print(self.errors["missingClass"])
        elif args[0] in self.classes:
            instances = str(models.storage.all().keys())
            print(instances.count(args[0]))
        else:
            print(self.errors["wrongClass"])

    def default(self, line):
        """Handle default behaviour"""
        funcs = {"all": self.do_all, "count": self.count, "show": self.do_show,
                 "destroy": self.do_destroy, "update": self.do_update}
        cmd = line.split('.', 1)
        class_name = cmd[0]
        args = [None]
        if len(cmd) > 1:
            args = cmd[1].strip("()").split('(')
        if args[0] in funcs:
            func = funcs[args[0]]
            params = class_name + ' '
            if len(args) > 1:
                if args[0] == "update" and args[1][-1] == '}':
                    str_dict = args[1].split(' ', 1)[1]
                    upd_dict = ast.literal_eval(str_dict)
                    params += args[1].split(',', 1)[0] + ' '
                    for k, v in upd_dict.items():
                        fparams = '{} "{}" "{}"'.format(params, str(k), str(v))
                        func(fparams)
                    return
                else:
                    params += args[1].replace(',', '')
            func(params)
        else:
            print("*** Unknown syntax: {}".format(line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
