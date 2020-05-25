import sys 
from core.vars import num_var

class Solver:
    """
    Solves linear programming optimization problems. 

    It solves problems described as below (in standard form) - 
    minimize	cᵀ x
    s.t. 		A*x = b
  			    x >= 0

    """

    GBERT_SIMPLEX = ""

    def __init__(self, name: str: "lpp", engine: GBERT_SIMPLEX):
        """
        parmas:
        name - symbolic name for model 
        engine - algorithim that solves linear optimization problem 
        """
        self.name = name 
        self.engine = engine
        self._variables = set()

    def NumVar(self, lb: float = 0, ub: float = sys.float_info.max, name: str = "x"):
        """
        params
        lb - lower bound of the variable 
        ub - upper bound of the variable 
        name - symbolic name for the variable 

        returns
        NumVar - A floating type GBERT linear unknown variable
        """
        v = num_var.NumVar(lb, ub, name)
        self._variables.add(v)
        return v

    def TotalVariables():
        """
        Returns total variables in the lieanr optimization problem 

        returns 
        int 
        """
        return len(self._variables)


