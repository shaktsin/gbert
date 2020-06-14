import sys 
import core.vars.num_var as nv
from core.vars.expression import Expression 

class Solver:
    """
    Solves linear programming optimization problems. 

    It solves problems described as below (in standard form) - 
    minimize	cᵀ x
    s.t. 		A*x = b
  			    x >= 0

    """

    MAX = "maximize"
    MIN = "minimize"
    GBERT_SIMPLEX = ""

    def __init__(self, name: str = "lpp", engine: str = GBERT_SIMPLEX):
        """
        parmas:
        name - symbolic name for model 
        engine - algorithim that solves linear optimization problem 
        """
        self.name = name 
        self.engine = engine
        self._variables = set()
        self._constraints = set()
        self._expression = None
        self._method = self.MAX

    def NumVar(self, lb: float = 0, ub: float = sys.float_info.max, name: str = "x"):
        """
        params
        lb - lower bound of the variable 
        ub - upper bound of the variable 
        name - symbolic name for the variable 

        returns
        NumVar - A floating type GBERT linear unknown variable
        """
        v = nv.NumVar(lb, ub, name)
        self._variables.add(v)
        return v

    def TotalVariables(self):
        """
        Returns total variables in the lieanr optimization problem 

        returns 
        int 
        """
        return len(self._variables)

    def AddConstraint(self, expression: Expression):
        self._constraints.add(expression)

    def SetObjective(self, expression: Expression, method: str = MAX):
        self._expression = expression
        self._method = method

    def Solve(self):
        return None

    


    


