import inspect

class Command:
    '''
        An object that represents a single command within the CLI.
    '''
    def __init__(self, **kwargs):
        '''
            Initialize a new command for our CLI.
            Name - Command primary Name
            Aliases - list alternative command names
            Func - Reference to whatever function this should call. This can be a lambda.
        '''
        self.name = kwargs.get('name')  # name
        self.alias = [x.lower() for x in kwargs.get('aliases')]  # alias list
        self.args = [] # args
        self.ref = kwargs.get('func')
        self.args = inspect.signature(self.ref).parameters
        self.desc = inspect.getdoc(self.ref) or None
        
        if set(self.args).intersection({'args', 'kwargs'}):
            raise TypeError("No args or kwargs at this time in commands.")
        
    def invoke(self, inputs):
        '''
            Invoke a command.
            Potentially return a result. 
            Completely up to the command if it feels the need to give feedback to the user.
            PS: You should absolutely give feedback to the user.
            :inputs: A dictionary containing the arguments as passed
        '''
        for arg in self.args:
            if arg not in inputs:
                raise TypeError("Command {} expects {} of type {}.".format(self.name, arg, self.args[arg].annotation))
            if self.args[arg].annotation is int:
                # try to convert int arguments to ints
                try:
                    inputs[arg] = int(inputs[arg])
                except ValueError:
                    # Raise a type error instead of a conversion error since this must be a non int in a place requiring an int
                    raise TypeError("Command {} expects {} of type {}.".format(self.name, arg, self.args[arg].annotation))
                    
        self.ref(**inputs)