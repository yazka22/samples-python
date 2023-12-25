# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:27:24 2022

@author: Yazka
"""
#1
import numpy
def cal_pop_fitness(equation_inputs, pop) :
    fitness = numpy.sum(pop*equation_inputs, axis=1)

    return fitness

#2
def select_mating_pool(pop, fitness, num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

#3
def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    crossover_point = numpy.uint8(offspring_size[1]/2)
    for k in range(offspring_size[0]):
# Indexul primului părinte care s-a împerecheat.
        parent1_idx = k%parents.shape[0]
# Indexul celui de-al doilea părinte care s-a împerecheat.
        parent2_idx = (k+1)%parents.shape[0]
# Noua descendență va avea prima jumătate din genele sale prelevate de la primul părinte.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
# Noul urmaș va avea a doua jumătate a genelor sale preluate de la al doilea părinte.

        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

#4
def mutation(offspring_crossover):
# Mutația schimbă o singură genă în fiecare urmaș la întâmplare.
    for idx in range(offspring_crossover.shape[0]):
# Valoarea aleatorie care trebuie adăugată genei.
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + random_value
    return offspring_crossover
