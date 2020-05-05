import numpy as np
from population import Population
from numpy.polynomial.polynomial import polyval
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

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


goal = -0.015
p = Population(goal, dummy_func_1)
print(p.main())

nbins = 30
ymax = 10
xmin = -1
bins = np.linspace(xmin, 0, nbins + 1)
fig, ax = plt.subplots(figsize=(10, 6))


def generation_fit(gen):
    return [x.fitness for x in gen.individuals]


def animate(i):
    ax.cla()
    ax.set(xlim=(xmin, 0), ylim=(0, ymax))

    mean_fit = p.generations[i].mean_fitness()
    best_fit = p.generations[i].top_fitness().fitness
    n_individuals = len(p.generations[i].individuals)
    best_new_fit = max([x.fitness for x in p.generations[i].individuals[1:]])

    ax.set_title('Histogram of fitness for individuals of each generation')
    ax.hist(generation_fit(p.generations[i]), bins, range=(xmin, 0), density=True, color='c')
    generations = ax.add_artist(Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0,
                                          label=f'Generation: {i}'))
    mean = ax.vlines([mean_fit], 0, ymax, linestyles='dashed', colors='k', label="Mean Fitness: {mean:.4f}".format(
        mean=mean_fit))
    goal_line = ax.vlines([goal], 0, ymax, linestyles='dashed', colors='g', label="Goal: {goal:.4f}".format(goal=goal))
    best_new = ax.vlines([best_new_fit], 0, ymax, linestyles='dashed', colors='m', label="Top Fitness (born this gen.):"
                                                                                     " {top:.4f}".format(top=best_fit))
    best = ax.vlines([best_fit], 0, ymax, linestyles='dashed', colors='r', label="Top Fitness: {top:.4f}".format(
        top=best_fit))
    ax.legend([generations, mean, goal_line, best, best_new], (f'Generation: {i} ({n_individuals} indiv.)',
                                                               "Mean Fitness: {mean:.4f}".format(mean=mean_fit),
                                                               "Goal: {goal:.4f}".format(goal=goal),
                                                               "Top Fitness (all time): {top:.4f}".format(top=best_fit),
                                                               "Top Fitness (born this gen.):{top:.4f}".format(
                                                                   top=best_new_fit)),

              loc='upper left')


animate(0)
anim = animation.FuncAnimation(fig, animate, interval=100, frames=len(p.generations) - 1)

# Writer = animation.FFMpegWriter(fps=30, codec='libx264')

anim.save("fitness_histo.mp4")

plt.draw()
plt.show()

