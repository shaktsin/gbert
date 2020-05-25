import sys

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


    def __str__(self):
        return "NumVar(lb={}, ub={}, name={}".format(self.lb, self.ub, self.name)
