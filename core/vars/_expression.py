class Expression:

    def __init__(self, operand_one, operand_two, operator="+"):
        self.operator = operator
        self.operand_one = operand_one
        self.operand_two = operand_two

    def __str__(self):
        return "{}(operator={}, operand_one={}, operand_two={})".format(self.__class__.__name__, self.operator, self.operand_one, self.operand_two)

    def __str__(self):
        return "{}(operator={}, operand_one={}, operand_two={})".format(self.__class__.__name__, self.operator, self.operand_one, self.operand_two)

    def __add__(self, other):
        return Expression(self, other, "+")

    def __radd__(self, other):
        return Expression(other, self, "+")