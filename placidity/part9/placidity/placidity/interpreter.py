import inspect

class Commands(list):
    def __init__(self, commands=None):
        commands = commands if commands else []

        if not hasattr(commands, '__iter__'):
            commands = [commands]
        
        super(Commands, self).__init__(commands)

    def match(self, expression):
        priorities = ('high', 'normal', 'low')

        for priority in priorities:
            commands = self.find(priority=priority)

            for command in commands:
                if command.matches(expression):
                    return command

    def find(self, name=None, priority=None):
        if name:
            for command in self:
                class_name = command.__class__.__name__

                if class_name.lower() == name:
                    return command

        if priority:
            return filter(lambda command: command.priority == priority, self)

class Interpreter:

    def __init__(self, commands=None):
        self.commands = Commands(commands)
        self.variables = {}

    def interpret(self, expression):
        possible_parameters = {'commands': self.commands,
            'expression': expression, 'variables': self.variables}

        try:
            command = self.commands.match(expression)
            args = self._get_args(command.execute)
            params = self._find_parameters(possible_parameters, args)

            return command.execute(**params)
        except:
            return 'null'

    def _get_args(self, method):
        return inspect.getargspec(method).args

    def _find_parameters(self, possible_parameters, args):
        ret = {}
        
        for name, value in possible_parameters.items():
            if name in args:
                ret[name] = value

        return ret
