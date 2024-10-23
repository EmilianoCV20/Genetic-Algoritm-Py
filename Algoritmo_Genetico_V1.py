import random
import numpy as np

#Inicializacion de la poblacion
def initialize_population(num_individuals):
    # Valores de la tabla proporcionada
    population = [
        [12, 5, 23, 8],  # Individuo 1
        [2, 21, 18, 3],  # Individuo 2
        [10, 4, 13, 14], # Individuo 3
        [20, 1, 10, 6],  # Individuo 4
        [1, 4, 13, 19],  # Individuo 5
        [20, 5, 17, 1]   # Individuo 6
    ]
    return population

#Calculo de la fx
def calculate_fx(population):
    fx_values = []
    for individual in population:
        a, b, c, d = individual
        fx = (a + 2*b + 3*c + 4*d) - 30
        fx_values.append(fx)
    return fx_values

#Calculo de la funcion objetivo (fitness)
def calculate_fitness(population):
    fitness_values = []
    for individual in population:
        a, b, c, d = individual
        fx = (a + 2*b + 3*c + 4*d) - 30
        fitness = 1/(1+fx)
        fitness_values.append(fitness)
    return fitness_values

#Calculo de la probabilidad de seleccion
def calculate_probabilities(fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]
    return probabilities

#Acumulacion de la probabilidad de seleccion
def accumulate_probabilities(probabilities):
    accumulated_probabilities = []
    accumulated = 0
    for p in probabilities:
        accumulated += p
        accumulated_probabilities.append(accumulated)
    return accumulated_probabilities

#Numeros random entre 0 y 1 para seleccion de individuos
def random_probabilities(population):
    random_probabilities = []
    for _ in range(len(population)):
        random_probabilities.append(random.random())
    return random_probabilities

#Seleccion de individuos segun el Random [i] > C[i] && C[i] < C[i+1]


#-----------------------------------------------------------

# Ejecución del algoritmo genético
def genetic_algorithm():
    num_individuals = 6  # 6 individuos
    print("\nNumero de individuos:", num_individuals)
    
    # Inicializacion
    population = initialize_population(num_individuals)
    print("\nPoblacion inicial:", population)
    
    # Calcular fx
    fx_values = calculate_fx(population)
    print("\nValores de fx:", fx_values)

    # Calcular fitness
    fitness_values = calculate_fitness(population)
    print("\nValores de fitness:", fitness_values)
    
    # Calcular probabilidades
    probabilities = calculate_probabilities(fitness_values)
    print("\nProbabilidades de seleccion:", probabilities)

    # Acumulacion de la probabilidad de seleccion
    accumulated_probabilities = accumulate_probabilities(probabilities)
    print("\nProbabilidades acumuladas de seleccion:", accumulated_probabilities)

    # Random [i]
    random = random_probabilities(population)
    print("\nRandom [i] (0-1):", random)

    # Seleccion de individuos

if __name__ == "__main__":
    genetic_algorithm()
