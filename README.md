# AirBnB clone - The console

## Project Learning Objectives

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Project Description

This project introduces fundamental concepts involved in Web Application
Architectures. In this part of the learning trajectory, we specifically focus on
the technologies/methodologies involved with data modeling and in general,
development framework.
The point of departure in this project is building a command interpreter (aka
the console) that will manage objects as we move towards building a
fully-fledged modern web application.

## The Console

The console or command line interpreter is a custom shell that allows a user to
work with a program interactively. The console makes it possible to automate
almost anything. For this project we use the console to manipulate objects; for
example: create and destroy an object, do operations on said objects, retrieve
and/or update objects.

## Usage

clone the repo into your home folder
```
https://github.com/rkbrian/AirBnB_clone
```
change into directory

### How to start it

Fire-up the executable ``console.py``
```
user@computer:~/AirBnB_clone$ ./console.py
```
The command prompt should be started and waiting for input

```
(hbnb)
```

### How to use it

Interactively, use the "help" command to see what commands the console can
interpret (minimal output)

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb) quit
$
```
The console should also work in non-interactive mode
```
$ echo help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```
### The real juice - Examples
```
~/AirBnB_clone $ ./console.py
(hbnb) create BaseModel
41bc14d1-9a38-4448-b35a-0aef96609d9d
(hbnb) all
["[BaseModel] (41bc14d1-9a38-4448-b35a-0aef96609d9d) {'created_at': datetime.datetime(2021, 5, 24, 14, 37, 28, 546201), 'updated_at': datetime.datetime(2021, 5, 24, 14, 37, 28, 546236), 'id': '41bc14d1-9a38-4448-b35a-0aef96609d9d'}"]
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy 41bc14d1-9a38-4448-b35a-0aef96609d9d
** class doesn't exist **
(hbnb) destroy BaseModel 41bc14d1-9a38-4448-b35a-0aef96609d9d
(hbnb) quit
$
```
