import numpy as np
from population import Population

TARGET = np.random.rand(16)


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


p = Population(-0.5, dummy_func_2)
print(p.main())
