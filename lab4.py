from abc import ABC, abstractmethod
 
 
class AbstractOperation(ABC):
 
    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__()
    
    @abstractmethod
    def execute(self):
        pass

class AddOperation(AbstractOperation):
    def execute(self):
        return self.operand_a + self.operand_b
 
 
class SubtractOperation(AbstractOperation):
    def execute(self):
        return self.operand_a - self.operand_b
 
 
class MultiplyOperation(AbstractOperation):
    def execute(self):
        return self.operand_a * self.operand_b
 
 
class DivideOperation(AbstractOperation):
    def execute(self):
        return self.operand_a / self.operand_b


operation = AddOperation(1, 2)
print("ADD = ",operation.execute())
# 3
operation = SubtractOperation(8, 2)
print("SUB = ",operation.execute())
# 6
operation = MultiplyOperation(8, 2)
print("MULT =",operation.execute())
# 16
operation = DivideOperation(8, 2)
print("DIV = ",operation.execute())
# 4.0


