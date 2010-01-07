from placidity.interpreter import Interpreter
 
class TestInterpreter:
 
    def setup_method(self, method):
        self.interpreter = Interpreter()
 
    def test_sum(self):
        assert self.interpreter.interpret('1+1') == 2
 
    def test_subtract(self):
        assert self.interpreter.interpret('5-1') == 4
 
    def test_multiply(self):
        assert self.interpreter.interpret('3*5') == 15
 
    def test_divide(self):
        assert self.interpreter.interpret('12/4') == 3



