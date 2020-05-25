class Var(object):
    """
    Generic variable type, having some common properties
    """

    def __init__(self, name: str = "x"):
        """
        name - Variable symbolic name 
        """
        self.name = name

    
    def __str__(self):
        return "Var(name={})".format(self.name)