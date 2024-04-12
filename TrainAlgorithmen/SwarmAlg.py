import random
import math

import numpy as np



#Schwarm algorithmus


def objective_function(x):
    # Hier die zu optimierende Funktion definieren
    return x**2  # Beispiel: Quadrat der Eingabe

def particle_swarm_optimization(objective_function, num_particles=10, num_dimensions=1, max_iterations=100, inertia_weight=0.5, cognitive_weight=2.0, social_weight=2.0):
    # Initialisiere Partikelpositionen und -geschwindigkeiten zufällig
    particles_position = np.random.rand(num_particles, num_dimensions)
    particles_velocity = np.random.rand(num_particles, num_dimensions)

    # Initialisiere die besten Positionen der Partikel
    personal_best_positions = particles_position.copy()
    personal_best_values = np.apply_along_axis(objective_function, 1, particles_position)

    # Initialisiere die globale beste Position
    global_best_position = particles_position[np.argmin(personal_best_values)]
    global_best_value = np.min(personal_best_values)

    # Haupt-Schleife des PSO
    for iteration in range(max_iterations):
        # Aktualisiere Partikelpositionen und -geschwindigkeiten
        inertia_term = inertia_weight * particles_velocity
        cognitive_term = cognitive_weight * np.random.rand() * (personal_best_positions - particles_position)
        social_term = social_weight * np.random.rand() * (global_best_position - particles_position)

        particles_velocity = inertia_term + cognitive_term + social_term
        particles_position += particles_velocity

        # Aktualisiere die besten Positionen der Partikel
        current_values = np.apply_along_axis(objective_function, 1, particles_position)
        update_indices = current_values < personal_best_values
        personal_best_positions[update_indices] = particles_position[update_indices]
        personal_best_values[update_indices] = current_values[update_indices]

        # Aktualisiere die globale beste Position
        if np.min(personal_best_values) < global_best_value:
            global_best_position = particles_position[np.argmin(personal_best_values)]
            global_best_value = np.min(personal_best_values)

        # Ausgabe des Fortschritts (optional)
        #print(f"Iteration {iteration+1}/{max_iterations}: Global Best Value = {global_best_value}")

    return global_best_position, global_best_value

# Beispielaufruf
best_position, best_value = particle_swarm_optimization(objective_function, num_particles=10, num_dimensions=1, max_iterations=100)
print(f"Optimale Position: {best_position}, Optimierter Wert: {best_value}")
