import numpy as np
from population import Population
from numpy.polynomial.polynomial import polyval

TARGET = np.random.rand(16)


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
    test_range = np.linspace(0, 1, n_samples)
    target = polyval(test_range, TARGET, tensor=False)
    output = polyval(test_range, input_array, tensor=False)
    loss = np.sum(abs(target - output)) / n_samples
    return -1 * loss

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
    output = np.array(input_array)
    loss = np.sum(abs(TARGET - output))
    return -1 * loss


p = Population(-0.02, dummy_func_2)
print(p.main())
