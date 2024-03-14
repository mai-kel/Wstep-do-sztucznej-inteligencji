import matplotlib.pyplot as plt
from solver import Evolution

def plot_tsp_solution(cities: list, cities_indexes: list):
    plt.figure()
    for i in range(len(cities_indexes) - 1):
        x = [cities[cities_indexes[i]][0], cities[cities_indexes[i+1]][0]]
        y = [cities[cities_indexes[i]][1], cities[cities_indexes[i+1]][1]]
        plt.plot(x, y, color="black", zorder=1)
        plt.scatter(x, y, s=300, c='blue', zorder=2)
    x = [cities[cities_indexes[0]][0], cities[cities_indexes[-1]][0]]
    y = [cities[cities_indexes[0]][1], cities[cities_indexes[-1]][1]]
    plt.plot(x, y, color="black", zorder=1)
    plt.scatter(x, y, s=300, c='blue', zorder=2)

def plot_best_individual_over_iterations(iterations_list, bests_list):
    plt.figure()
    plt.plot(iterations_list, bests_list)
    plt.ylabel("Długość najkrótszej ścieżki")
    plt.xlabel("Numer iteracji")
    plt.title("Najkrótsza droga w zależności od numeru iteracji")

cities = [[35, 51], [113, 213], [82, 280], [322, 340], [256, 352], [160, 24], [322, 145], [12, 349],
          [282, 20], [241, 8], [398, 153], [182, 305], [153, 257], [275, 190], [242, 75], [19, 229],
          [303, 352], [39, 309], [383, 79], [226, 343]]

evolution_params = {
    "population_size": 100,
    "mutation_chance": 0.6,
    "mutation_force": 1,
    "crossover_chance": 0.8,
    "max_iterations": 800,
    "cities": cities
}

evolution = Evolution()
answer = evolution.get_answer(evolution_params['population_size'], evolution_params["cities"],
                              evolution_params["mutation_chance"], evolution_params["mutation_force"],
                              evolution_params["crossover_chance"], evolution_params["max_iterations"])

iterations_list, bests_list = evolution.get_best_over_iterations(evolution_params['population_size'], evolution_params["cities"],
                                                                 evolution_params["mutation_chance"], evolution_params["mutation_force"],
                                                                 evolution_params["crossover_chance"], evolution_params["max_iterations"])

plot_tsp_solution(evolution_params["cities"], answer.city_indexes)
plot_best_individual_over_iterations(iterations_list, bests_list)

plt.show()