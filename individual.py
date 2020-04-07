class Individual:
    """
    Attributes: genes which is default to None
                fit_func
                fitness = None
                
    """
    def __init__(self, genes, fit_func):
        self.genes = genes
        self.fit_func = fit_func
        
    def assess_fit(self):
        
    """
    Assesses fitness based on self.fit_func
    """
        ## self.fitness = fitness
    
    def reproduce(self, other):
    """
    Creates children/child with parents 'self' and 'other'.
    Args: 
        other (individual): Mate with which self has a child    
    Returns:
        individual: child individual with parents self and other
    
    
    """
