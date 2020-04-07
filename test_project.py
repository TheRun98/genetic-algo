import unittest
from generation import Generation
from individual import Individual 
from population import Population 

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