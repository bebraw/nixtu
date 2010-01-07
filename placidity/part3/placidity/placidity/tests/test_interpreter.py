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
 
class TestPrintVariables(TestInterpreter):
    command = 'variables'
 
    def test_print_none(self):
        assert self.interpret(self.command) == 'No stored variables'
 
    def test_print_variables(self):
        self.interpret('a=14')
        self.interpret('b=-4')
        self.interpret("animal='boar'")
        assert self.interpret(self.command) == "Stored variables:\n" + \
            "a=14\nb=-4\nanimal='boar'"

class TestCleanVariables(TestInterpreter):
 
    def test_clean_none(self):
        assert self.interpret('vars') == 'No stored variables'
        self.interpret('clean')
        assert self.interpret('vars') == 'No stored variables'
 
    def test_clean_variables(self):
        self.interpret('a=12')
        assert self.interpret('vars') == 'Stored variables:\na=12'
        self.interpret('clean')
        assert self.interpret('vars') == 'No stored variables'

class TestHelp(TestInterpreter):
 
    def test_just_help(self):
        assert self.interpret('help') == 'clean - Cleans up stored' + \
            ' variables\nvariables, vars - Shows stored variables'
 
    def test_specific_help(self):
        assert self.interpret('help clean') == 'Cleans up stored variables'

class TestMath(TestInterpreter):
    operations = Operations(('1+1', 2), ('5-1', 4), ('3*5', 15), ('12/4', 3), )
 
    def test_operations(self):
        for operation in self.operations:
            assert self.interpret(operation.expression) == operation.result
