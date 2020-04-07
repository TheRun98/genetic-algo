

class Population:
    """
    has a list of Generation objects as an attribute, and appends new 
    ‘generations’ to the list as the old ones reproduce. Continues this cycle 
    until either a maximum number of generations is reached or the 
    fitness reaches a target value.
    
    Attributes:
        fitness_func: function used to asses fitness of indivduals.
        target_value: target fitness at which main() will stop.
        generations: An Array of generations.

    Driver: Kosta | Navigator: Ben
    """

    def __init__(self, target_value, fitness_func):
        """
        
        Args:
            target_value(float): target fitness
            fitness_func(func): function for assessing fitness of individuals
        
        """
        
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
    def __str__(self):
        output = ""
        for i, g in enumerate(self.generations):
            output += f"Generation {i}:\n {str(g)}"
        return output