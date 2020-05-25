import sys
from numbers import Number
from ._var import Var
from ._expression import Expression

class NumVar(Var):
    """
    Floating Point Variable Declarator
    """

    def __init__(self, lb: float = 0, ub: float = sys.float_info.max, name: str = "x"):
        """
        @params
        lb - lower bound of the variable 
        ub - upper bound of the variable 
        name - symbolic name for the variable 
        """
        Var.__init__(self, name)
        self.lb = lb
        self.ub = ub
        self.val = 0

    def __str__(self):
        return "{}(lb={}, ub={}, name={})".format(self.__class__.__name__, self.lb, self.ub, self.name)

    def __repr__(self):
        return "{}(lb={}, ub={}, name={})".format(self.__class__.__name__, self.lb, self.ub, self.name)

    def __add__(self, other):
        """
        add operation overloading to support expression
        """

        if not isinstance(other, Expression) and not isinstance(other, NumVar):
            raise ValueError("Invalid add operation on NumVar. Must be added with expression or NumVar") 

        if isinstance(other, NumVar):
            other = Expression(self, 1, "*") 

        return Expression(self, 1, "*") + other

    def __radd__(self, other):
        """
        reverse add operation overloading to support expression
        """

        if not isinstance(other, Expression) and not isinstance(other, NumVar):
            raise ValueError("Invalid add operation on NumVar. Must be added with expression or NumVar") 

        if isinstance(other, NumVar):
            other = Expression(self, 1, "*") 

        return other + Expression(self, 1, "*") 

    def __mul__(self, other):
        """
        mult operation overloading to support expression
        """

        if not isinstance(other, Number):
            raise ValueError("Invalid mult operation on NumVar. Must be multiplied with a number") 

        return Expression(self, other, "*")

    def __rmul__(self, other):
        """
        reverse mult operation overloading to support expression
        """

        if not isinstance(other, Number):
            raise ValueError("Invalid mult operation on NumVar. Must be multiplied with a number") 

        return Expression(other, self, "*")
