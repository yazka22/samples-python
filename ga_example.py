# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:49:27 2022

@author: Yazka
"""

import numpy
import ga
# Input-ul ecuației.
equation_inputs = [4,-2,3.5,5,-11,-4.7]
# Numărul de ponderi.
num_weights = 6
"""
Parametrii algoritmului genetic:
Mating pool size = Dimensiunea selectata pentru împerechere (nr. parinti)
Population size = Mărimea populației
"""
sol_per_pop = 8
num_parents_mating = 4
# Definirea mărimii populației
# Populatia va avea sol_per_pop cromozomi, unde fiecare cromozom va avea num_weights gene
pop_size = (sol_per_pop,num_weights) 
#Crearea populatiei initiale.
new_population = numpy.random.uniform(low=-4.0, 
high=4.0, size=pop_size)
print(new_population)
num_generations = 3
for generation in range(num_generations):
 print("Generation : ", generation)
# Calcularea funcției fitness pentru fiecare cromozom.
fitness = ga.cal_pop_fitness(equation_inputs, new_population)
# Selectia celor mai buni parinti.
parents = ga.select_mating_pool(new_population, fitness, 
num_parents_mating)
# Generarea urmatoarei generatii folosind crossover.
offspring_crossover = ga.crossover(parents, offspring_size=(pop_size[0]-
parents.shape[0], num_weights))
# Adaugarea unor variabile pentru descendenti folosind mutatia
offspring_mutation = ga.mutation(offspring_crossover)
# Crearea noii populatii bazate pe parinti si descendenti
new_population[0:parents.shape[0], :] = parents
new_population[parents.shape[0]:, :] = offspring_mutation
# Cel mai bun rezultat pentru iterația curenta.
print("Best result : ", numpy.max(numpy.sum(new_population*equation_inputs, 
axis=1)))
# Obținerea celei mai bune soluții după terminarea tuturor generațiilor.
#La început, fitnessul este calculat pentru fiecare soluție din generația finală.
fitness = ga.cal_pop_fitness(equation_inputs, new_population)
# Apoi returnam indicele acelei soluții corespunzând celei mai bune condiții de fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))
print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])


