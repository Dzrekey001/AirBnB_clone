# AirBnB Clone - The Console

This project is part of the AirBnB clone project and focuses on building a command-line interpreter to manage AirBnB objects. The command interpreter allows users to create, retrieve, update, and delete objects, as well as perform various operations on them.

***
**Getting Started**

To start the console, simply run the console.py script. This will launch the command-line interface, where you can interact with the AirBnB objects.

```bash
$ ./console.py
The console will display a prompt (hbnb), indicating that it's ready to accept commands. You can start typing commands and press Enter to execute them.
```
***
**Commands**

The console supports the following commands:

1. quit or EOF: Exit the program.

2. help: Display help information about the available commands.

3. create: Create a new instance of a specified class and save it.

4. show: Print the string representation of an instance based on the class name and ID.

5. destroy: Delete an instance based on the class name and ID.

6. all: Print all string representations of instances or all instances of a specified class.

7. update: Update an instance based on the class name and ID by adding or updating attributes.

***
Examples
Here are some examples of using the command interpreter:

```bash
$ ./console.py
(hbnb) create User
f6d0a1bb-5e58-4f4b-a734-4b11e48e8396
(hbnb) show User f6d0a1bb-5e58-4f4b-a734-4b11e48e8396
[User] (f6d0a1bb-5e58-4f4b-a734-4b11e48e8396) {'id': 'f6d0a1bb-5e58-4f4b-a734-4b11e48e8396', 'created_at': '2023-07-11T10:00:00.000000', 'updated_at': '2023-07-11T10:00:00.000000'}
(hbnb) update User f6d0a1bb-5e58-4f4b-a734-4b11e48e8396 email "test@example.com"
(hbnb) show User f6d0a1bb-5e58-4f4b-a734-4b11e48e8396
[User] (f6d0a1bb-5e58-4f4b-a734-4b11e48e8396) {'id': 'f6d0a1bb-5e58-4f4b-a734-4b11e48e8396', 'created_at': '2023-07-11T10:00:00.000000', 'updated_at': '2023-07-11T10:00:00.000000', 'email': 'test@example.com'}
(hbnb) all User
[[User] (f6d0a1bb-5e58-4f4b-a734-4b11e48e8396) {'id': 'f6d0a1bb-5e58-4f4b-a734-4b11e48e8396', 'created_at': '2023-07-11T10:00:00.000000', 'updated_at': '2023-07-11T10:00:00.000000', 'email': 'test@example.com'}]
(hbnb) quit
$
```
***
**Authors**

This project was developed by:

Daniel Dzrekey

***
**Contributions**

We welcome contributions to this project. If you would like to contribute, please submit a pull request on GitHub.
