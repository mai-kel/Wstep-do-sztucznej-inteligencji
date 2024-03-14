import random
import math
import numpy as np
import copy

class Individual:
    def __init__(self, cities: list, generate_randomly: bool, city_indexes: list = None) -> None:
        self.cities = cities
        if generate_randomly:
            self.city_indexes = list(np.random.choice(range(len(cities)),
                                            len(cities), replace=False))
        else:
            self.city_indexes = city_indexes

        self.normalize()
        self.evaluate()

    def mutate(self, mutation_force):
        for i in range(mutation_force):
            rand1 = random.randint(0, len(self.city_indexes)-1)
            rand2 = random.randint(0, len(self.city_indexes)-1)
            self.city_indexes[rand1], self.city_indexes[rand2] = self.city_indexes[rand2], self.city_indexes[rand1]
        self.normalize()
        self.evaluate()

    def cross(self, other):
        indexes_replaced_dict = {}
        half_len = len(self.city_indexes)//2
        for i in range(half_len, len(self.city_indexes)):
            indexes_replaced_dict[self.city_indexes[i]] = other.city_indexes[i]
        new_indexes = other.city_indexes[:half_len]
        new_indexes.extend(self.city_indexes[half_len:])

        for i in range(half_len):
            while new_indexes[i] in new_indexes[half_len:]:
                new_indexes[i] = indexes_replaced_dict.pop(new_indexes[i])

        return Individual(self.cities, False, new_indexes)

    def evaluate(self):
        def calc_dist(point1, point2):
            return math.dist(point1, point2)
        value = 0
        for i in range(len(self.city_indexes) - 1):
            value += calc_dist(self.cities[self.city_indexes[i]],
                               self.cities[self.city_indexes[i+1]])

        value += calc_dist(self.cities[self.city_indexes[0]],
                               self.cities[self.city_indexes[-1]])

        self.value = -value

    def normalize(self):
        """
        Function shifts city indexes list elements so that element with value 0 was first
        """
        while self.city_indexes[0] != 0:
            self.city_indexes.append(self.city_indexes.pop(0))



class Population:
    def __init__(self, generate_randomly: bool, cities: list, population_size: int = None , individuals: list = None) -> None:
        self.cities = cities
        if not generate_randomly:
            self.individuals: list = individuals
        else:
            self.individuals = []
            for i in range(population_size):
                self.individuals.append(Individual(cities, True))

    def reproduce(self, num_of_individuals):
        new_population = []
        while len(new_population) < num_of_individuals:
            new_population.append(copy.deepcopy(max(random.choices(self.individuals, k=2), key=lambda x: x.value)))
        return Population(False, self.cities, individuals=new_population)

    def genetic_operations(self, mutation_prob, mutation_force, crossover_chance):
        children = []
        for individual in self.individuals:
            if random.randint(0, 100) < crossover_chance*100:
                children.append(individual.cross(random.choice(self.individuals)))
        self.individuals.extend(children)

        for individual in self.individuals:
            if random.randint(0, 100) < mutation_prob*100:
                individual.mutate(mutation_force)


class Evolution:
    def __init__(self) -> None:
        pass

    def succession(self, population: Population, new_population: Population, cities: list):
        next_population = []
        next_population.append(max(population.individuals, key=lambda x: x.value))
        next_population.extend(new_population.individuals)
        return Population(False, cities, individuals=next_population)


    def get_answer(self, population_size, cities, mutation_chance, mutation_force,
                    crossover_chance, max_iterations):
        iterations = 0
        population = Population(True, cities, population_size)
        best_individual = max(population.individuals, key=lambda x: x.value)
        while iterations < max_iterations:
            new_population = population.reproduce(population_size)
            new_population.genetic_operations(mutation_chance, mutation_force, crossover_chance)
            if best_individual.value < max(new_population.individuals, key=lambda x: x.value).value:
                best_individual = max(new_population.individuals, key=lambda x: x.value)
            population = self.succession(population, new_population, cities)
            iterations += 1

        return best_individual

    def get_best_over_iterations(self, population_size, cities, mutation_chance, mutation_force,
                                crossover_chance, max_iterations):
        best_value_list = []
        iterations_list = []
        iterations = 0
        population = Population(True, cities, population_size)
        best_individual = max(population.individuals, key=lambda x: x.value)
        while iterations < max_iterations:
            new_population = population.reproduce(population_size)
            new_population.genetic_operations(mutation_chance, mutation_force, crossover_chance)
            if best_individual.value < max(new_population.individuals, key=lambda x: x.value).value:
                best_individual = max(new_population.individuals, key=lambda x: x.value)
            population = self.succession(population, new_population, cities)
            iterations += 1
            best_value_list.append(-best_individual.value)
            iterations_list.append(iterations)

        return (iterations_list, best_value_list)


def measure_avg_misscalculation(evolution_params, estimation, n):
    population_size = evolution_params["population_size"]
    mutation_chance = evolution_params["mutation_chance"]
    mutation_force = evolution_params["mutation_force"]
    max_iterations = evolution_params["max_iterations"]
    crossover_chance = evolution_params["crossover_chance"]
    cities = evolution_params["cities"]
    evolution = Evolution()
    average_output = sum(-evolution.get_answer(population_size, cities, mutation_chance, mutation_force,
                                               crossover_chance, max_iterations).value for i in range(n))/n
    return abs(average_output - estimation)





