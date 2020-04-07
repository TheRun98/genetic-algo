class Individual:
    """ Class that represent an individual
    
    Attributes: 
        genes: default is None
        fit_func (func): 
                
    """
    def __init__(self, genes, fit_func):
        self.genes = genes
        self.fit_func = fit_func
        
    def assess_fit(self):   
         """ Assess fitness based on self.fit_func """
        ## self.fitness = fitness
    
    def reproduce(self, other):
        """ Creates child with parents 'self' and 'other'.
        Args:
            other (individual): Mate with which self has a child    
        Returns:
            individual: child individual with parents self and other
        """
