#!/usr/bin/python3
"""Model that serves a the entry point for the program"""
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines all the classes for the console"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Doesn't do anything on ENTER and emptyline.
        """
        pass

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def do_EOF(self, line):
        """handles the end of file interupt"""
        print()
        return True

    def do_quit(self, line):
        """exit the program when quit is passed as the arguments"""
        print()
        return True

    def do_create(self, line):
        """create a new object of a specified class"""
        if line == "":
            print("** class name missing **")

        elif line not in storage.classes().keys():
            print("** class doesn't exist **")
        else:
            new_model = storage.classes()[line]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """print out the object instance atributes when a id is passed"""
        arguments = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif arguments[0] not in storage.classes().keys():
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif f"{arguments[0]}.{arguments[1]}" not in storage.all().keys():
            print("** no instance found **")
        else:
            all_obj = storage.all()
            target = all_obj[f"{arguments[0]}.{arguments[1]}"]
            print(target)

    def do_destroy(self, line):
        """Deletes an object from the storage"""
        arguments = line.split(" ")
        if line == "":
            print("** class name missing **")
        elif arguments[0] not in storage.classes().keys():
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        elif f"{arguments[0]}.{arguments[1]}" not in storage.all().keys():
            print("** no instance found **")
        else:
            all_obj = storage.all()
            all_obj.pop(f"{arguments[0]}.{arguments[1]}")
            storage.save()

    def do_count(self, line):
        """count the number of instances created"""

        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_all(self, line):
        """ print all the object in the storage; passing a class name will
            print all objects of the class
        """
        all_objects = storage.all()
        if line != "":
            if line not in storage.classes().keys():
                print("** class doesn't exist **")
            else:
                for key, value in all_objects.items():
                    if key.split(".")[0] == line:
                        print(str(value))
        else:
            for key, value in all_objects.items():
                print(str(value))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
