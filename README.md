# AirBnB clone - The console

The console is a simple command interpreter to manage objects (Create a new object, retrieve an object, do operations, update attributes of an object and destroy an object)

## Usage
### Interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
### Non-Interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Authors
Gabriel Montaño - [@exploitpnk](https://twitter.com/exploitpnk)\
Cristian Murcia - [@pechefeliz](https://twitter.com/pechefeliz)