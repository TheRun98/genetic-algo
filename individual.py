class Individual:
    """ Class that represents an individual
    
    Attributes: 
        genes: default is None
        fit_func (func): 
                
    """

    def __init__(self, genes, fit_func):
        """
        Args:
            genes(array): an array of 16 attributes representing the individual's characteristics
            fit_func(func): function for assessing fitness
        """
        self.genes = genes
        self.fit_func = fit_func
        self.fitness = -1

    def assess_fit(self):
        """ Assesses fitness based on self.fit_func and stores it it in self.fit"""
        # self.fitness = self.fit_func(self.genes)

    def reproduce(self, other):
        """ Creates child with parents 'self' and 'other'.
        Args:
            other (individual): Mate with which self has a child    
        Returns:
            individual: child individual with parents self and other
        """

    def __str__(self):
        return str(self.fitness) + ": " + str(self.genes)
