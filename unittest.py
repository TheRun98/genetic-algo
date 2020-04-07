import unittest
import generation as gen
import individual as indv 
import population as pop 

class TestGeneticAlgo(unittest.TestCase):
    
    def setUp(self):
        genes = []
        func = None
        self.individual = indv.Individual(genes, func)
        self.generation = gen.Generation([self.individual])
        self.population = pop.Population(func)
        
    def test_generation(self):
        self.assertTrue(self.generation.__str__() == "")
        
    def test_individual(self):
        self.assertTrue(self.individual.__str__() == "")
        
    def test_population(self):
        self.assertTrue(self.population.__str__() == "")
        
if __name__ == "__main__":
    unittest.main()