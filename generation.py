class Generation:
    """ This class represents a generaion of individuals
    
    Attributes:
        individuals (list): list of individuals
        fitness_func (func): function used to assess fitness of individuals
    
    """
    
    def __init__(self, indiv, fit_func):
        self.individuals = indiv
        self.fitness_func = fit_func
         
    def reproduction(self):
        """ Produces the next generation
        
        Returns:
            Generation: new generation object consisting of individuals 
            decended from self.individuals
        """
    
    def fitness(self):
        """ Assess the fitness of individuals in the generation by calling 
        fitness method of members self.individuals """
        for i in self.individuals:
            i.assess_fit()
        
    def __str__(self):
        output = ""
        for i in self.individuals:
            output += str(i) + "\n"
        return output