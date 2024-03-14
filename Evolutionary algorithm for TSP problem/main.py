import argparse
import ast
from solver import Evolution

def get_cities_from_file(path):
    with open(path, 'r') as handler:
        text = handler.read()
        cities = ast.literal_eval(text)
        return cities

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('population_size', type=int)
    parser.add_argument('cities_path', type=str)
    parser.add_argument('mutation_chance', type=float)
    parser.add_argument('mutation_force', type=float)
    parser.add_argument('cross_chance', type=float)
    parser.add_argument('max_iterations', type=int)

    args = parser.parse_args()

    population_size = int(args.population_size)
    mutation_chance = float(args.mutation_chance)
    mutation_force = int(args.mutation_force)
    max_iterations = int(args.max_iterations)
    crossover_chance = float(args.cross_chance)
    cities_path = args.cities_path
    cities = get_cities_from_file(cities_path)

    evolution = Evolution()
    answer = evolution.get_answer(population_size, cities, mutation_chance,
                                   mutation_force, crossover_chance, max_iterations)

    print(f'Length of the shortest path found is: {-answer.value}')
    print("City indexes of found solution:")
    print(answer.city_indexes)

