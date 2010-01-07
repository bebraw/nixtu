class Interpreter:
 
    def __init__(self):
        self.vars = {}
 
    def interpret(self, expression):
        try:
            return eval(expression, self.vars)
        except NameError:
            return 'null'
        except SyntaxError:
            l_value, r_value = expression.split('=')
            
            try:
                self.vars[l_value] = int(r_value)
            except ValueError:
                self.vars[l_value] = self.interpret(r_value)