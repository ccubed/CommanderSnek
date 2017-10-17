from .Command import Command
import inspect
import sys

class Pycom:
    def __init__(self, subcls=None):
        self.commands = {}

        if subcls and inspect.isclass(subcls):
            funcs = [x for x in subcls.__dict__.keys() if inspect.isfunction(subcls.__dict__[x]) and x != '__init__']
            for fun in funcs:
                self.add_command(subcls.__dict__[fun])

        if len(sys.argv) > 1:
            if sys.argv[1] == '-c':
                if sys.argv[2] in self.commands:
                    self.parse(self.commands[sys.argv[2]], sys.argv[3:])
                else:
                    self.do_help()
            else:
                if sys.argv[1] in self.commands:
                    self.parse(self.commands[sys.argv[1]], sys.argv[2:])
                else:   
                    self.do_help()
        else:
            self.do_help()

    def parse(self, command, command_line):
        inputs = {}
        current_value = None
        while True:
            try:
                item = command_line.pop(0)
                if '-' in item:
                    if not current_value:
                        current_value = [item, '']
                    else:
                        inputs[current_value[0].replace('-','')] = current_value[1].strip()
                        current_value = [item, '']
                else:
                    current_value[1] += " {}".format(item)
            except IndexError:
                break
            finally:
                if current_value[1]:
                    inputs[current_value[0].replace('-','')] = current_value[1].strip()

        command.invoke(inputs)

    def add_command(self, function, name=None, alias=None):
        if not inspect.isfunction(function):
            raise TypeError("Expected a callable but did not get one.")
            
        fn = function.__name__ if not name else name
        fa = [] if not alias else alias
        
        self.commands[fn] = Command(name=fn, aliases=fa, func=function)
        
    def do_help(self):
        print("You entered an unrecognized command.\nDisplaying help for this program.\n")
        for command in self.commands:
            help_txt = "{}".format(self.commands[command].name)
            if self.commands[command].desc:
                help_txt += "\t-\t{}".format(self.commands[command].desc)
            help_txt += "\nArguments Accepted:\n"
            for param in self.commands[command].args:
                help_txt += "\t{}: {}\n".format(param, self.commands[command].args[param].annotation)
            print(help_txt)