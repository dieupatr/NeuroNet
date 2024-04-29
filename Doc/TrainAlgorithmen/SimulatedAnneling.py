import random
import math

import numpy as np




#minimum

def f(x):
    # Beispiel-Funktion, die optimiert werden soll
    return x**2

def simulated_annealing(initial_x, temperature, cooling_rate, max_iterations):
    current_x = initial_x
    best_x = current_x
    current_cost = f(current_x)
    best_cost = current_cost

    for iteration in range(max_iterations):
        # Generate a neighboring solution
        neighbor_x = generate_neighbor(current_x)

        # Calculate the cost of the neighbor solution
        neighbor_cost = f(neighbor_x)

        # Decide whether to accept the neighbor solution
        if neighbor_cost < current_cost or random.random() < acceptance_probability(current_cost, neighbor_cost, temperature):
            current_x = neighbor_x
            current_cost = neighbor_cost

        # Update the best solution if needed
        if current_cost < best_cost:
            best_x = current_x
            best_cost = current_cost

        # Cool down the temperature
        temperature *= cooling_rate

    return best_x, best_cost

def generate_neighbor(x):
    # Beispiel: Erzeugen einer benachbarten Lösung durch Hinzufügen eines kleinen zufälligen Werts
    return x + random.gauss(0, 1.0)

def acceptance_probability(current_cost, neighbor_cost, temperature):
    if neighbor_cost < current_cost:
        return 1.0
    return math.exp((current_cost - neighbor_cost) / temperature)

# Beispielaufruf:
initial_x = 0.0
initial_temperature = 100.0
cooling_rate = 0.99
max_iterations = 1000

best_x, best_cost = simulated_annealing(initial_x, initial_temperature, cooling_rate, max_iterations)

print("Beste x:", best_x)
print("Beste Kosten:", best_cost)


