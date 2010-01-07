from placidity.interpreter import Interpreter
from placidity.utils import Operations
 
class TestInterpreter:
 
    def setup_method(self, method):
        interpreter = Interpreter()
        self.interpret = interpreter.interpret

class TestSetVariable(TestInterpreter):
 
    def test_set(self):
        self.interpret('a=6')
        assert self.interpret('a') == 6
 
    def test_set_expression(self):
        self.interpret('a=4*3')
        assert self.interpret('a') == 12
 
    def test_set_variable(self):
        self.interpret('a=8')
        self.interpret('b=a')
        assert self.interpret('b') == 8
 
    def test_variable_in_expression(self):
        self.interpret('a=12')
        assert self.interpret('a+3') == 15

class TestUnsetVariable(TestInterpreter):
 
    def test_unset_variable(self):
        assert self.interpret('a') == 'null'
 
    def test_variable_in_expression(self):
        assert self.interpret('a+3') == 'null'
 
class TestMath(TestInterpreter):
    operations = Operations(('1+1', 2), ('5-1', 4), ('3*5', 15), ('12/4', 3), )
 
    def test_operations(self):
        for operation in self.operations:
            assert self.interpret(operation.expression) == operation.result
