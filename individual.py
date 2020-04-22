import random
SEX_PARAM = [0.25, 0.5, 0.9]

class Individual:
    """ Class that represents an individual
    
    Attributes: 
        genes(array): array of 16 floats representing the individual's characteristics
        fit_func(func): function used to assess fitness of the individual
        fitness(float): a float representing the individual's fitness, stored so it doesn't have to be evaluated every
            time the value is used, default None

    (Ben w/ Charlie)
    """

    def __init__(self, genes, fit_func):
        """
        Args:
            genes(array): an array of 16 floats representing the individual's characteristics
            fit_func(func): function for assessing fitness
        """
        if genes is None:
            self.genes = [random.uniform(0, 1) for x in range(16)]
        else:
            self.genes = genes
        self.fit_func = fit_func
        self.fitness = None

    def assess_fit(self):
        """ Assesses fitness based on self.fit_func and stores it it in self.fit"""
        self.fitness = self.fit_func(self.genes)
        return self.fitness

    def reproduce(self, other):
        """ Creates child with parents 'self' and 'other'.
        Args:
            other (individual): Mate with which self has a child    
        Returns:
            individual: child individual with parents self and other
        """
        child = Individual(None, self.fit_func)
        for i in range(16):
            child.inherit_gene(i, self, other)
        return child

    def inherit_gene(self, index, mother, father):
        """ Sex inherited gene by self.reproduce
        Args:
            index (int): index of genes
            mother (Individual): mother
            father (Individual): father
        Side Effects:
            Assigns new value to self.genes[index]
        """
        rand = random.uniform(0, 1)
        if rand <= SEX_PARAM[0]:
            self.genes[index] = mother.genes[index] # inherit from mother
        elif SEX_PARAM[0] < rand <= SEX_PARAM[1]:
            self.genes[index] = father.genes[index] # inherit from father
        elif SEX_PARAM[1] < rand <= SEX_PARAM[2]: 
            self.genes[index] = self.mean([father.genes[index], mother.genes[index]]) # average of parents
        else:
            self.genes[index] = random.uniform(0, 1)
        return

    def mean(self, lst):
        """ Finds the mean of a list of numbers
        
        Args:
            lst (list): list of numbers
        
        Return:
            (Int): the mean of the provided list
            
        Driver: Yazeed | Navigator: Ben
        """
        n = len(lst)
        sum = 0
        for i in lst:
            sum += i
        return (sum/n)   
        
    def __str__(self):
        return str(self.fitness) + ": " + str(self.genes)

    