from generation import Generation


class Population:
    """
    A population list of Generation objects as an attribute, and appends new 
    ‘generations’ to the list as the old ones reproduce. Continues this cycle 
    until either a maximum number of generations is reached or the 
    fitness reaches a target value.
    
    Attributes:
        fitness_func (func): function used to asses fitness of indivduals.
        target_value (float): target fitness at which main() will stop.
        generations (list): An Array of generations.

    Driver: Kosta | Navigator: Ben
    """

    def __init__(self, target_value, fitness_func, sex_param=(0.25, 0.5, .9), length=200, gen_size=50):
        self.fitness_func = fitness_func
        self.target_value = target_value
        self.generations = list()
        self.new_generation()
        self.sex_param = sex_param
        self.length = length
        self.gen_size = gen_size

    def new_generation(self):
        """
        Makes a new generation object based on the last generation object 
        in self.generations and appends it to self.generations.
        
        Driver: Kosta | Navigator: Ben
        """
        if len(self.generations) == 0:
            gen = Generation(None, self.fitness_func, sex_param=self.sex_param, size=self.gen_size)
        else:
            gen = self.generations[-1].reproduction()
        self.generations.append(gen)
        return

    def main(self):
        """
        creates new generations until the fitness of the fittest member of a 
        generation is greater than or equal to self.target_fitness
        
        Returns:
            individual: fittest individual

        Driver: Ben | Navigator: Kosta
        """
        gens = 0
        top_fitness = 0
        fittest = None

        while gens < self.length:
            gens += 1
            self.new_generation()
            fittest = self.generations[-1].top_fitness()
            top_fitness = fittest.fitness
            print("Gen {gens} ({size} individuals): {top_new:.4f} [{top_fitness:.4f}] (avg: {mean_fitness:.4f})".format(
                gens=gens,
                size=len(self.generations[-1].individuals),
                top_new=max([x.fitness for x in self.generations[-1].individuals[1:]]),
                top_fitness=top_fitness,
                mean_fitness=self.generations[-1].mean_fitness()))
            if top_fitness >= self.target_value:
                break
        return fittest

    def __str__(self):
        output = ""
        for i, g in enumerate(self.generations):
            output += f"Generation {i}:\n {str(g)}"
        return output
