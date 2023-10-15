#!/usr/bin/python3
from models import storage
import json
import cmd
import re
import ast


class HBNBCommand(cmd.Cmd):
    """Main class definition for the console module"""

    prompt = "(hbnb) "

    def precmd(self, line):
        """
        Description:    Intercepts command in the
                        form <class name>.<commnand>() and
                        format to execute commands on the classes.
        Usage:
            (hbnh) <class name>.all()
            (hbnh) <class name>.count()
            (hbnh) <class name>.destroy(<id>)
            (hbnh) <class name>.update(<id>, <attribute name>,
            <attribute value>)
        """
        command = line
        regex = r"(?:\s+)?(\w+)\.(\w+)\((.+?)?\)"
        result = re.match(regex, command)

        if result:
            class_name = result.group(1)
            do_command = result.group(2)
            arguments = result.group(3)
            if do_command and class_name:
                command = "{} {}".format(do_command, class_name)
                if arguments:
                    reg = r"""^(?:\"([a-f0-9-]+)\")?(?:(?:\s*,\s*\"(.+?)\")
                                ?\s*,\s*(\".+?\")|\s*,\s*(\{.*?\}))?$
                            """
                    arg_result = re.match(reg, arguments)
                    if arg_result:
                        if class_id := arg_result.group(1):
                            command = "{} {}".format(command, class_id)
                        if dictionary := arg_result.group(4):
                            command = "{} {}".format(command, dictionary)
                        elif class_attr := arg_result.group(2):
                            command = "{} {}".format(command, class_attr)
                            if class_val := arg_result.group(3):
                                command = "{} {}".format(command, class_val)

        return cmd.Cmd.precmd(self, command)

    def do_count(self, line):
        """
            Description:    retrieves the number of instances if a class.

            Usage:
                (hbnb) <class name>.count()
                (hbnb) count <class name>
        """
        line_dict = line.split(" ")
        if line_dict[0] == "":
            total_count = "** class name missing ***"
        elif line_dict[0] in storage.classes():
            total_count = len([k for k in storage.all().keys()
                               if k.startswith(line_dict[0])])
        else:
            total_count = "** class doesn't exist **"
        print(total_count)

    def check_if_dict(self, dictionary):
        """Function to check if if an input is a dictionary"""

        to_dict = None
        try:
            to_dict = ast.literal_eval(dictionary)
        except Error:
            pass
        return to_dict

    def do_update(self, line):
        """
        Description:
                Update an instance based on the class name and id
                by adding or updating attribute. Save the changes
                into the json file.

        Usage:
            (hbnb) update <class name> <class id> <attribute name>
            <attribute value>
        """
        regex = r"""^(\w+)?\s([a-f0-9-]+)?(?:\s([^\"]+?)?
                    \s\"(.+?)?\"|\s(\{.+?\}))?
                """
        result = re.search(regex, line)
        class_name = result.group(1)
        class_id = result.group(2)
        class_attr = result.group(3)
        attr_value = result.group(4)
        dictionary = self.check_if_dict(result.group(5))

        key = "{}.{}".format(class_name, class_id)
        if class_name is None:
            print("** class name missing **")
        elif class_id is None:
            print("** instance id missing **")
        elif class_attr is None and dictionary is None:
            print("** attribute name missing **")
        elif attr_value is None and dictionary is None:
            print("** value missing **")
        elif key in storage.all().keys():
            obj = storage.all()[key]
            if dictionary:
                for key, value in dictionary.items():
                    setattr(obj, key, value)
                obj.save()
            else:
                setattr(obj, class_attr, attr_value)
                obj.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
            Description:
                        Prints all string representation of all instances based
                        based or not on the class name.

            Usage:
                (hbnh) all
                (hbnh) all <class name>
        """
        line = line.split(" ")
        if line[0] == "":
            str_rep = [obj.__str__() for obj in storage.all().values()]
        elif line[0] in storage.classes().keys():
            str_rep = [obj.__str__() for obj in storage.all().values()
                       if line[0] == obj.to_dict()["__class__"]]
        else:
            str_rep = "** class does't exist **"

        print(str_rep)

    def do_destroy(self, line):
        """
            Description:    Deletes an instance based on the call name and id.
                            Save changes to json file.

            Usage:
                (hbnb) destroy <class name> <class id>
        """

        cls_and_id = line.split(" ")

        if line == "":
            print("** class name missing **")
        elif cls_and_id[0] not in storage.classes().keys():
            print("** class doesn't exit **")
        else:
            try:
                key = "{}.{}".format(cls_and_id[0], cls_and_id[1])

                if key in storage.all().keys():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_show(self, line):
        """
            Description:    Prints the string representation of an instance
                            based on the class name and id

            Usage:
                (hbnh) show <class name> <class id>
        """

        cls_and_id = line.split(" ")

        if line == "":
            print("** class name missing **")
        elif cls_and_id[0] not in storage.classes().keys():
            print("** class doesn't exit **")
        else:
            try:
                key = "{}.{}".format(cls_and_id[0], cls_and_id[1])

                if key in storage.all().keys():
                    obj = storage.all()[key]
                    print(obj)
                else:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_create(self, line):
        """
            Description:    Create a new instance of class and save it to
                            a json file.

            Usage:
                (hbnb) create <class name>
        """

        if line == "":
            print("** class name missing **")
        elif cls := storage.classes().get(line):
            tmp_class = cls()
            tmp_class.save()
            print(tmp_class.id)
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """
            Description: command to exit the console.

            Usage:
                (hbnb) quit
        """
        return True

    def emptyline(self):
        """
            Description:    an empty line + enter would not execute and
                            command.
        """
        pass

    def do_EOF(self, line):
        """
            Description: Interrupting with EOF should exit the console

            Usage:
                key press ctrl + D
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
