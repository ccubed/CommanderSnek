# CommanderSnek
Create command line interfaces based on classes you've already written!
I saw a couple of tools roll out, but they were built using 2.7 toolbases and rather complicated code sources. I asked myself why and I didn't find an answer. So I made a tool to create CLI interfaces from pre-rolled classes or functions myself. It's simple, powerful and extensible. Also, it's based on Python 3.5 and 3.6, so you can have all kinds of fun while knowing that it's not going to go the way of the dodo bird anytime soon. (And if you're thinking shots fired, then yeah, shots fired.)

# How's this work bro
Commander Snek - though really, that's a long name for the file, so we'll call the class Pycom - works by being given a class object and then reading all the functions off that object. These functions become your commands and your resulting help document - so make sure you write a help doc! All that matters from there is that your script is called from the command line with options and arguments. Arguments should be in the format `-<argument> <value>` and the first item in the command string should be the command to be called. From there, Commander Snek will invoke your command to do whatever you want it to do. 

## How about an example
Say this is random.py
```py
from Pycom import Pycom

class test:
    def add(a:int, b:int):
        '''
            Add two numbers
        '''
        print(a+b)

if __name__=='__main__':
    Pycom(test)
```
And then we call this as:
`python random.py add -a 4 -b 6`
And then we'll get out:
`10`

### Ok, but what if I typed ad
Then you'd get
```
You entered an unrecognized command.
Displaying help for this program.

add     -       Add 2 numbers
Arguments Accepted:
        a: <class 'int'>
        b: <class 'int'>
```

### Ok, but what if I put in an invalid argument
Then you'd get
```
TypeError: Command add expects a of type <class 'int'>.
```

### Do I need to convert the ints?
Nope, I got that.

# What about more docs!
Coming soon