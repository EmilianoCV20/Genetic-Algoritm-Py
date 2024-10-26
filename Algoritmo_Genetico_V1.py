import random
import math

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

#Rango de seleccion segun la acumulacion de la probabilidad de seleccion y random [i]
def select_individuals(population, accumulated_probabilities, random_probabilities):
    selected_individuals = []
    for random_probability in random_probabilities:
        for i, accumulated_probability in enumerate(accumulated_probabilities):
            if random_probability <= accumulated_probability:
                selected_individuals.append(population[i])
                break
    return selected_individuals

#Asignacion de nuevos valores a los individuos en la poblacion
def replace_individuals(population, selected_individuals):
    for i in range(len(population)):
        population[i] = selected_individuals[i]
    return population

# Selección de individuos para crossover basado en un umbral
def select_for_crossover(population, random_values, threshold=0.25):
    selected_individuals = []
    for i, r in enumerate(random_values):
        if r < threshold:
            selected_individuals.append(population[i])  # Individuo seleccionado para crossover
        else:
            selected_individuals.append("X")  # No seleccionado
    return selected_individuals

# Realización del crossover entre pares de individuos seleccionados, mostrando cada paso de manera compacta
def perform_crossover(population, selected_individuals):
    new_population = population[:]
    pairs = [i for i, ind in enumerate(selected_individuals) if ind != "X"]
    crossover_points = []
    paired_individuals = []
    
# Realización del crossover de manera asimétrica, asegurando que cada individuo seleccione su pareja sin repetir cambios
def perform_asymmetric_crossover(population, selected_individuals):
    new_population = population[:]
    pairs = [i for i, ind in enumerate(selected_individuals) if ind != "X"]
    crossover_points = []
    paired_individuals = []

    # Realizar crossover asimétrico
    for i in range(len(pairs) - 1):  # Iterar hasta el penúltimo seleccionado
        parent1 = pairs[i]
        parent2 = pairs[i + 1]  # El siguiente individuo como pareja
        paired_individuals.append([parent1 + 1, parent2 + 1])  # Guardar el par original para mostrar

        # Generar un punto de corte aleatorio
        crossover_point = random.randint(1, 3)
        crossover_points.append(crossover_point)

        # Intercambiar genes solo en el primer individuo, manteniendo el original en el segundo
        offspring1 = new_population[parent1][:crossover_point] + population[parent2][crossover_point:]
        new_population[parent1] = offspring1

    # El último individuo en la lista de seleccionados hace crossover con el primero
    if len(pairs) > 1:
        parent1 = pairs[-1]
        parent2 = pairs[0]
        paired_individuals.append([parent1 + 1, parent2 + 1])

        # Generar un punto de corte aleatorio
        crossover_point = random.randint(1, 3)
        crossover_points.append(crossover_point)

        # Intercambiar genes solo en el último individuo, manteniendo el original en el primero
        offspring1 = new_population[parent1][:crossover_point] + population[parent2][crossover_point:]
        new_population[parent1] = offspring1

    return paired_individuals, crossover_points, new_population

#---Mutación---
# Parámetros de mutación
mutation_rate = 0.1
total_genes = 24

# Calcular número de mutaciones
num_mutations = math.floor(mutation_rate * total_genes)

# Aplicar mutaciones
def apply_mutation(population, num_mutations):
    new_population = [chromosome[:] for chromosome in population]  # Copia de la población

    # Generar posiciones para la mutación
    mutation_positions = random.sample(range(total_genes), num_mutations)

    for pos in mutation_positions:
        # Determinar en qué cromosoma y en qué gen se encuentra la posición
        chrom_index = pos // len(population[0])
        gene_index = pos % len(population[0])

        # Valor original antes de la mutación
        original_value = new_population[chrom_index][gene_index]

        # Generar nuevo valor para el gen (entre 0 y 30)
        new_value = random.randint(0, 30)
        
        # Mostrar información de mutación
        #print(f"Mutating chromosome {chrom_index + 1}, gene {gene_index + 1}: original value = {original_value}, new value = {new_value}")
        print(f"Mutando cromosoma {chrom_index + 1}, gen {gene_index + 1}: valor original = {original_value}, nuevo valor = {new_value}")


        # Aplicar mutación
        new_population[chrom_index][gene_index] = new_value

    return new_population


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
    random_values = random_probabilities(population)
    print("\nRandom [i] (0-1):", random_values)

    # Rango de seleccion segun la acumulacion de la probabilidad de seleccion y random [i]
    selected_individuals = select_individuals(population, accumulated_probabilities, random_values)
    print("\nIndividuos seleccionados:", selected_individuals)

    # Asignacion de nuevos valores a los individuos en la poblacion
    population = replace_individuals(population, selected_individuals)
    print("\nPoblacion actualizada:", population)

    # Random [i] para crossover
    random_values2 = random_probabilities(population)
    print("\nRandom [i] (0-1) para crossover:", random_values2)

    # Selección de individuos para crossover con umbral
    selected_for_crossover = select_for_crossover(population, random_values2)
    print("\nIndividuos seleccionados para crossover: ", selected_for_crossover)

    # Realizar el crossover
    paired_individuals, crossover_points, new_population = perform_asymmetric_crossover(population, selected_for_crossover)
    print("\nPares seleccionados para crossover:", paired_individuals)
    print("\nPuntos de corte por cada par:", crossover_points)
    print("\nPoblacion despues del crossover:", new_population)
    print(" ")

    # Aplicar mutaciones y obtener la nueva población
    new_population = apply_mutation(population, num_mutations)
    print("\nNueva poblacion (despues de la mutacion):", new_population)
    #for chrom in new_population: print(chrom)


if __name__ == "__main__":
    genetic_algorithm()