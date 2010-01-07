

class Command(object):
 
    def matches(self, expression):
        if hasattr(self.aliases, '__iter__'):
            return expression in self.aliases
 
        return expression == self.aliases
 
class Clean(Command):
    aliases = 'clean'
    description = 'Cleans up stored variables'
 
    def execute(self, interpreter):
        interpreter.vars = {}
 
class Help(Command):
    aliases = 'help'
 
    def matches(self, expression):
        parts = expression.split()
 
        if parts[0] == 'help':
            if len(parts) > 1:
                self.target = parts[1]
            else:
                self.target = None
 
            return True
 
    def execute(self, interpreter):
        ret = ''
 
        if self.target:
            target_command = interpreter.commands.match(self.target)
            
            return target_command.description
        else:
            for command in interpreter.commands:
                if hasattr(command, 'description'):
                    if hasattr(command.aliases, '__iter__'):
                        ret += ', '.join(command.aliases)
                    else:
                        ret += command.aliases
    
                    ret += ' - ' + command.description + '\n'
 
        return ret.rstrip()
 
class Variables(Command):
    aliases = ('variables', 'vars', )
    description = 'Shows stored variables'
 
    def execute(self, interpreter):
        variable_str = ''
 
        for name, value in interpreter.vars.items():
            if isinstance(value, str):
                value_str = "'" + value + "'"
            else:
                value_str = str(value)
 
            variable_str += '\n' + name + '=' + value_str
 
        if variable_str:
            return 'Stored variables:' + variable_str
 
        return 'No stored variables'
 
class Commands(list):
 
    def __init__(self):
        commands = (Clean(), Help(), Variables(), )
        super(Commands, self).__init__(commands)
 
    def match(self, expression):
        for command in self:
            if command.matches(expression):
                return command
