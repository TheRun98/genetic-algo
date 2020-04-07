# Population class: has a list of Generation objects as an attribute, 
# and appends new ‘generations’ to the list as the old ones die. 
# Continues this cycle until either a maximum number of generations 
# is reached or the fitness reaches a target value. (Kosta)

class Population:
    """
    A class for..
    
    Attributes:
        fitness_func: function used to asses fitness of indivduals.
        generations: An Array of generations.

    """

    def __init__(self, target_value, fitness_func):
        """
        
        Attributes:
            target_value(float): target fitness
            fitness_func(): 
        
        """
        
        self.target_value
        self.fitness_func
        
    def new_generation(self):
        """
        Makes a new generation object based on the last generation object 
        in self.generations and appends it to self.generations.
        
        """
        
    def main(self):
        """
        creates new generations until the fitness of the fittest member of a 
        generation is greater than or equal to self.target_fitness
        
        Returns:
            individual: fittest individual
        
        """
