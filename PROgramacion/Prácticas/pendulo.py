import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuración inicial de la simulación
G = 6.67430e-11  # Constante gravitacional (m^3 kg^-1 s^-2)
dt = 1e5  # Paso de tiempo (segundos)
n_steps = 1000  # Número de pasos de la simulación

# Clase para representar cada cuerpo celeste
class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.force = np.zeros(2)

# Función para calcular las fuerzas gravitacionales entre cuerpos
def compute_forces(bodies):
    for body in bodies:
        body.force = np.zeros(2)  # Reiniciar fuerza
    for i, body_a in enumerate(bodies):
        for j, body_b in enumerate(bodies):
            if i != j:
                r = body_b.position - body_a.position
                distance = np.linalg.norm(r) + 1e-3  # Evitar divisiones por cero
                force_magnitude = G * body_a.mass * body_b.mass / distance**2
                body_a.force += force_magnitude * r / distance

# Función para actualizar las posiciones y velocidades de los cuerpos
def update_bodies(bodies, dt):
    for body in bodies:
        # Integración de Verlet
        acceleration = body.force / body.mass
        body.position += body.velocity * dt + 0.5 * acceleration * dt**2
        new_acceleration = body.force / body.mass
        body.velocity += 0.5 * (acceleration + new_acceleration) * dt

# Inicialización de los cuerpos
bodies = [
    Body(1.989e30, [0, 0], [0, 0]),  # Sol
    Body(5.972e24, [1.496e11, 0], [0, 29.78e3]),  # Tierra
    Body(6.39e23, [2.279e11, 0], [0, 24.07e3])   # Marte
]

# Configuración para la visualización
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2e11, 2e11)
ax.set_ylim(-2e11, 2e11)
points, = ax.plot([], [], 'bo', markersize=5)

# Función para inicializar la animación
def init():
    points.set_data([], [])
    return points,

# Función para actualizar los datos de la animación
def animate(frame):
    compute_forces(bodies)
    update_bodies(bodies, dt)
    positions = np.array([body.position for body in bodies])
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=n_steps, init_func=init, blit=True, interval=20)
plt.show()
