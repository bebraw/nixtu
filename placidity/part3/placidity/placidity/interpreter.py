from commands import Commands
 
class Interpreter:
 
    def __init__(self):
        self.commands = Commands()
        self.vars = {}
 
    def interpret(self, expression):
        matching_command = self.commands.match(expression)
 
        if matching_command:
            return matching_command.execute(self)
 
        try:
            return eval(expression, {}, self.vars)
        except NameError:
            return 'null'
        except SyntaxError:
            l_value, r_value = expression.split('=')
            
            try:
                self.vars[l_value] = int(r_value)
            except ValueError:
                self.vars[l_value] = self.interpret(r_value)
