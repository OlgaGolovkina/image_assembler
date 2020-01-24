"""Selects fittest individuals from given population."""
import random
import bisect


def roulette_selection(population, elites=4):
    """Roulette wheel selection.

    Each individual is selected to reproduce, with probability directly proportional to its fitness
    score.

    :params population: Collection of the individuals for selecting.
    :params elite:      Number of elite individuals passed to next generation.
    """
    fitness_values = [individual.fitness for individual in population]
    probability_intervals = [sum(fitness_values[:i + 1]) for i in range(len(fitness_values))]

    def select_individual():
        """Selects random individual from population based on fittest value"""
        random_select = random.uniform(0, probability_intervals[-1])
        selected_index = bisect.bisect_left(probability_intervals, random_select)
        return population[selected_index]

    selected = []
    for i in range(len(population) - elites):
        first, second = select_individual(), select_individual()
        selected.append((first, second))

    return selected
