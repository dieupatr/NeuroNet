import random
import math

import numpy as np



#maximum

def objective_function(x):
    # Hier deine Zielfunktion definieren
    return -x**2 # Beispiel: negative quadratische Funktion

def iterated_hill_climber(iterations, step_size, initial_solution):
    current_solution = initial_solution

    for _ in range(iterations):
        current_score = objective_function(current_solution)
        next_solution = current_solution + random.gauss(0, 1.0)
        next_score = objective_function(next_solution)

        if next_score > current_score:
            current_solution = next_solution

    return current_solution, objective_function(current_solution)

# Beispielaufruf
initial_solution = 0.0
iterations = 5
step_size = 0.1

best_solution, best_score = iterated_hill_climber(iterations, step_size, initial_solution)

print(f"Die beste gefundene Lösung ist {best_solution} mit einem Wert von {best_score}.")
