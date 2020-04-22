import random
from individual import Individual


class Generation:
    """ This class represents a generaion of individuals
    
    Attributes:
        individuals (list): list of individuals
        fitness_func (func): function used to assess fitness of individuals
    
    """

    def __init__(self, indiv, fit_func):
        if indiv is None:
            self.individuals = [Individual(None, fit_func) for x in range(50)]
        else:
            self.individuals = indiv
        self.fitness_func = fit_func

    def reproduction(self):
        """ Produces the next generation
        
        Returns:
            Generation: new generation object consisting of individuals 
            descended from self.individuals
            
        Driver: Yazeed | Navigator: Ben
        """
        fitnesses = [x.assess_fit() for x in self.individuals]
        mean_fit = self.mean(fitnesses)
        fit_indvs = [x for x in self.individuals if x.fitness > mean_fit]
        fit_indvs = fit_indvs.sort(key=[x.fitness for x in self.individuals if x.fitness > mean_fit])
        children = list()

        for indv in fit_indvs:
            for n in range(2):
                rand_indv = random.randint(0, (len(self.individuals) - 1))
                new_child = indv.reproduce(self.individuals[rand_indv])
                children.append(new_child)
            if len(children) > len(self.individuals):
                break

        return Generation(children, self.fitness_func)

    def fitness(self):
        """ Assess the fitness of individuals in the generation by calling 
        fitness method of members self.individuals

        Side Effects:
            updates self.fitness for all individuals
            
        Driver: Yazeed | Navigator: Ben
        """
        for indv in self.individuals:
            indv.assess_fit()

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
        return (sum / n)

    def top_fitness(self):
        """returns fit fittest individual

        Returns:
            fittest (Individual): individual with the highest fitness

        Driver: Ben | Navigator: Yazeed
        """
        self.fitness()
        return self.individuals[[x.fitness for x in self.individuals].index(max([x.fitness for x in self.individuals]))]

    def __str__(self):
        output = ""
        for i in self.individuals:
            output += str(i) + "\n"
        return output
