import numpy as np
from population import Population
from numpy.polynomial.polynomial import polyval
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D

TARGET = np.random.rand(16)
TARGET_2 = np.random.rand(16)
test_range = np.linspace(0, 1, 10_000)
target_poly = polyval(test_range, TARGET, tensor=False)

"""
This script is not technically part of the project, it just generates the animations we use in our presentation. As a 
result, its documentation and pair programming is not up to the standards of the project, and should not be considered 
beholden to those standards. It is outside the scope of the project as outlined in the proposal and is 
explicitly referenced as a piece of code that would be written but not considered part of the project in the 
proposal. It's included in the repository because it's cool, and because it allows anyone to see the algorithm in 
action with their own modifications, fitness functions, SEX_PARAMS, etc. While running this script is a good way to 
verify that the code in the project is working properly, it's not intended to be a test. That is the job of the 
unittests in test_project. 
"""


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
    output = polyval(test_range, input_array, tensor=False)
    loss = np.sum(abs(target_poly - output)) / n_samples
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


def generation_fit(gen):
    return [x.fitness for x in gen.individuals]

p_m = (0.001, 0.05, 0.25)
goal = -0.001
p1 = Population(goal, dummy_func_1, (.25, .5, 1-p_m[0]))
p2 = Population(goal, dummy_func_1, (.25, .5, 1-p_m[1]))
p3 = Population(goal, dummy_func_1, (.25, .5, 1-p_m[2]))
populations = (p1, p2, p3)

palette = ['#0b6e4f', '#2B4162', '#FA9F42', '#721817', '#419D78']

for p in populations:
    print(p.main())
# gen = 10

nbins = 100
ymax = 10
xmin = -1
# bins = np.linspace(xmin, 0, nbins + 1)
fig = plt.figure(figsize=(11, 7))
ax = fig.add_subplot(111, projection='3d')


# ax.set(xlim=(-1, 0), ylim=(0, 1), zlim=(0, 10))

# data_1 = np.full(201, 1).tolist()
# data_2 = np.full(201, 1).tolist()
# data_3 = np.full(201, 1).tolist()
# data = (data_1, data_2, data_3)
#
# x = np.linspace(-1, 0, nbins)
# z = np.zeros((3, 29))
# bins = np.zeros((3, 30))

def animate(f):
    ax.cla()
    ax.set(xlim=(xmin, 0), ylim=(0, 2), zlim=(0, 15))

    x = np.linspace(-1, 0, nbins)
    z = np.zeros((3, nbins-1))
    bins = np.zeros((3, nbins))

    for i, p in enumerate(populations):
        if f < len(p.generations):
            gen_fit = generation_fit(p.generations[f])
        else:
            continue

        # for j, l in enumerate(gen_fit):
        #     data[i][j] = l
        z[i], bins[i] = np.histogram(gen_fit, x, (-1, 0), density=False)

    for i, p in enumerate(populations):
        if f >= len(p.generations):
            continue

        mean_fit = p.generations[f].mean_fitness()
        best_fit = p.generations[f].top_fitness().fitness
        n_individuals = len(p.generations[f].individuals)
        best_new_fit = max([x.fitness for x in p.generations[f].individuals[1:]])
        best_new_fit_indiv = max(p.generations[f].individuals[1:], key=lambda x: x.fitness)
        best_new_fit_poly = polyval(test_range, best_new_fit_indiv.genes, tensor=False)
        best_fit_poly = polyval(test_range, p.generations[f].individuals[0].genes, tensor=False)

        ax.set_title(f'Histogram of fitness for populations with different P(mutation) (gen. {f})', pad=100.)
        ax.bar(bins[0][:-1], z[i], i + 0.005, 'y', width=0.035, color=palette[i])
        ax.bar([mean_fit], [15], i - 0.02, 'y', width=0.005, color='k')
        ax.bar([best_fit], [15], i - 0.02, 'y', width=0.005, color='r')
        ax.bar([best_new_fit], [15], i - 0.02, 'y', width=0.005, color='m')
        ax.text3D(-0.99, i, 12, f'P={p_m[i]}')
        ax.text3D(-0.99, i, 11, 'individuals: {mf}'.format(mf=n_individuals))
        ax.text3D(-0.99, i, 10, 'mean fit: {mf:.4f}'.format(mf=mean_fit))
        ax.text3D(-0.99, i, 9, 'best fit (all time): {mf:.4f}'.format(mf=best_fit))
        ax.text3D(-0.99, i, 8, 'best fit (born this gen.): {mf:.4f}'.format(mf=best_new_fit))

#     mean_fit = p.generations[i].mean_fitness()
#     best_fit = p.generations[i].top_fitness().fitness
#     n_individuals = len(p.generations[i].individuals)
#     best_new_fit = max([x.fitness for x in p.generations[i].individuals[1:]])
#     best_new_fit_indiv = max(p.generations[i].individuals[1:], key=lambda x: x.fitness)
#     best_new_fit_poly = polyval(test_range, best_new_fit_indiv.genes, tensor=False)
#     best_fit_poly = polyval(test_range, p.generations[i].individuals[0].genes, tensor=False)
#
#     ax1.set_title('Histogram of fitness for individuals of each generation')
#     ax1.hist(generation_fit(p.generations[i]), bins, range=(xmin, 0), density=True, color='c')
#     generations = ax1.add_artist(Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0,
#                                            label=f'Generation: {i}'))
#     mean = ax1.vlines([mean_fit], 0, ymax, linestyles='dashed', colors='k', label="Mean Fitness: {mean:.4f}".format(
#         mean=mean_fit))
#     goal_line = ax1.vlines([goal], 0, ymax, linestyles='dashed', colors='g', label="Goal: {goal:.4f}".format(
#     goal=goal))
#     best = ax1.vlines([best_fit], 0, ymax, linestyles='dashed', colors='r', label="Top Fitness: {top:.4f}".format(
#         top=best_fit))
#     best_new = ax1.vlines([best_new_fit], 0, ymax, linestyles='dashed', colors='m',
#                           label="Top Fitness (born this gen.):"
#                                 " {top:.4f}".format(top=best_fit))
#     ax1.legend([generations, mean, goal_line, best, best_new], (f'Generation: {i} ({n_individuals} indiv.)',
#                                                                 "Mean Fitness: {mean:.4f}".format(mean=mean_fit),
#                                                                 "Goal: {goal:.4f}".format(goal=goal),
#                                                                 "Top Fitness (all time): {top:.4f}".format(
#                                                                     top=best_fit),
#                                                                 "Top Fitness (born this gen.):{top:.4f}".format(
#                                                                     top=best_new_fit)),
#
#                loc='upper left')
#
#     ax2.set_title('Comparison between target curve and fittest individuals')
#     ax2.plot(test_range, best_fit_poly, color='r', label='Fittest (all time)')
#     ax2.plot(test_range, best_new_fit_poly, color='m', label='Fittest (born this gen.)')
#     ax2.plot(test_range, target_poly, color='k', lw=.75, label="Target Curve")
#     ax2.legend(loc='upper left')
#
#     ax3.set_title(r'$\Delta$ between target curve and fittest individuals')
#     ax3.plot(test_range, best_fit_poly - target_poly, color='r', label='Fittest (all time)')
#     ax3.plot(test_range, best_new_fit_poly - target_poly, color='m', label='Fittest (born this gen.)')
#     ax3.plot(test_range, np.zeros(test_range.shape), ls='--', lw=.75, color='k', label="Target Curve")
#     ax3.legend(loc='upper left')
#
#     ax4.set_title('Comparison between genes of target and fittest individuals')
#     ax4.bar(np.arange(0, 16), best_new_fit_indiv.genes - TARGET, color='m', align='edge', width=.4,
#             label='Fittest (born this gen.)')
#     ax4.bar(np.arange(0., 16.)+.4, p.generations[i].individuals[0].genes - TARGET, color='r', align='edge', width=.4,
#             label='Fittest (all time)')
#     ax4.plot(np.arange(0, 16), np.zeros(16), ls='--', lw=.75, color='k')
#     ax4.legend(loc='upper left')


animate(0)
anim = animation.FuncAnimation(fig, animate, interval=100, frames=max([len(x.generations) for x in populations]),
                               blit=False)

# only uncomment the below line if you have ffmpeg installed and are willing to wait for a while each time it runs with
# more than 100 generations.

anim.save("fitness_histo_3D_5.mp4")

plt.draw()
plt.show()
