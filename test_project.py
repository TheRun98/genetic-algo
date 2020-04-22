import unittest
import numpy as np
from numpy.polynomial.polynomial import polyval
from generation import Generation
from individual import Individual
from population import Population

np.random.seed(0)
TARGET = np.random.rand(16)
RANDOM_GENES_A = np.random.rand(16)
RANDOM_GENES_B = np.random.rand(16)
RANDOM_GENES_C = np.random.rand(16)


def dummy_func_1(input_array):
    """
    a sample fitness function that uses the closeness of fit to a polynomial with random coefficients to calculate
    fitness (loss)

    Args:
        input_array(array): iterable of 16 floats between 0 and 1

    Returns:
        loss(float): an approximation of how close the polynomial with coefficients determined by input is to the target
        polynomial

    (Ben)
    """
    n_samples = 10_000
    test_range = np.linspace(0, 100, n_samples)
    target = polyval(test_range, TARGET, tensor=False)
    output = polyval(test_range, input_array, tensor=False)
    loss = np.sum(abs(target - output)) / n_samples
    return loss

def dummy_func_2(input_array):
    """
    a sample fitness function that uses the closeness of fit to a linear equation to calculate fitness (loss)

    Args:
        input_array(array): iterable of 16 floats between 0 and 1

    Returns:
        loss(float): an approximation of how close the polynomial with coefficients determined by input is to the target
        linear equation

    (Ben)
    """
    n_samples = 10_000
    test_range = np.linspace(0, 100, n_samples)
    target = np.ndarray(TARGET)
    output = np.ndarray(input_array)
    loss = np.sum(abs(target - output)) / n_samples
    return -1 * loss


class TestGeneticAlgo(unittest.TestCase):

    def setUp(self):
        func = dummy_func_1
        self.individual_a = Individual(RANDOM_GENES_A, func)
        self.individual_b = Individual(RANDOM_GENES_B, func)
        self.individual_c = Individual(RANDOM_GENES_C, func)
        self.generation = Generation([self.individual_a, self.individual_b, self.individual_c], func)
        self.population = Population(0.25, func)

    def test_generation(self):
        """ General test of a generation output
        
            (Yazeed) 
        """
        self.assertTrue(self.generation.__str__() == "None: [0.0202184  0.83261985 0.77815675 0.87001215 0.97861834 "
                                                     "0.79915856\n 0.46147936 0.78052918 0.11827443 0.63992102 "
                                                     "0.14335329 0.94466892\n 0.52184832 0.41466194 0.26455561 "
                                                     "0.77423369]\nNone: [0.45615033 0.56843395 0.0187898  0.6176355  "
                                                     "0.61209572 0.616934\n 0.94374808 0.6818203  0.3595079  0.43703195"
                                                     " 0.6976312  0.06022547\n 0.66676672 0.67063787 0.21038256 "
                                                     "0.1289263 ]\nNone: [0.31542835 0.36371077 0.57019677 0.43860151 "
                                                     "0.98837384 0.10204481\n 0.20887676 0.16130952 0.65310833 0.2532916"
                                                     "  0.46631077 0.24442559\n 0.15896958 0.11037514 0.65632959 "
                                                     "0.13818295]\n")

    def test_individual(self):
        """ General test of an individual output
        
            (Yazeed & Charlie) 
        """
        self.assertTrue(self.individual_a.__str__() == "None: [0.0202184  0.83261985 0.77815675 0.87001215 0.97861834 "
                                                       "0.79915856\n 0.46147936 0.78052918 0.11827443 0.63992102 "
                                                       "0.14335329 0.94466892\n 0.52184832 0.41466194 0.26455561 "
                                                       "0.77423369]")

    def test_population(self):
        """ General test of a population output
        
            (Yazeed & Kosta)
        """
        self.assertTrue(self.population.__str__() == "")

    def test_individual_assess_fit(self):
        """(Ben w/ Charlie)"""
        self.individual_a.assess_fit()
        self.assertAlmostEqual(self.individual_a.fitness, 4.309953574343199e+28)

    def test_generation_fitness(self):
        """(Ben w/ Yazeed)"""
        self.generation.fitness()
        self.assertAlmostEqual(self.generation.individuals[0].fitness, 4.309953574343199e+28)
        
    def test_population_new_generation(self):
        """
        Driver: Kosta | Navigator: Yazeed
        """
        self.assertIn(self.individual_a, self.generation)
        self.assertIn(self.individual_b, self.generation)
        
    def test_population_validation(self):
        """
        Driver: Kosta | Navigator: Charlie
        """
        with self.assertRaises(ValueError):
            test1 = Population.Population("words", 6)
            # test2 = Population.Population(x, 1)

    def test_individual_init(self):
        i = Individual(None, dummy_func_2)
        print(i)

    def test_generation_init(self):
        g = Generation(None, dummy_func_2)
        print(g)

    def test_population_init(self):
        p = Population(-0.5, dummy_func_2)
        print(p)


if __name__ == "__main__":
    # unittest.main()
    p = Population(-0.5, dummy_func_2)