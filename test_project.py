import unittest
import numpy as np
from generation import Generation
from individual import Individual
from population import Population


def dummy_func(input_array):
    """
    a sample fitness function that uses the closeness of fit to a polynomial with random coefficients to calculate
    fitness (loss)

    Args:
        input_array(array): iterable of 16 floats between 0 and 1

    Returns:
        loss(float): an approximation of how close the polynomial with coefficients determined by input is to the target
        polynomial
    """
    n_samples = 10_000

    test_range = np.linspace(0, 100, n_samples)
    random_coefficients = np.random.rand((16,))
    target = np.polynomial.polyval(test_range, random_coefficients, tensor=False)
    output = np.polynomial.polyval(input_array, random_coefficients, tensor=False)
    loss = np.sum(abs(target - output)) / n_samples
    return loss


class TestGeneticAlgo(unittest.TestCase):

    def setUp(self):
        genes = []
        func = None
        self.individual = Individual(genes, func)
        self.generation = Generation([self.individual], func)
        self.population = Population([self.generation], func)

    def test_generation(self):
        self.assertTrue(self.generation.__str__() == "")

    def test_individual(self):
        self.assertTrue(self.individual.__str__() == "")

    def test_population(self):
        self.assertTrue(self.population.__str__() == "")


if __name__ == "__main__":
    unittest.main()
