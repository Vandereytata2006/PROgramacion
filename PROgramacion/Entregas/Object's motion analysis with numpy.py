import numpy as np
import matplotlib.pyplot as plt

# Define constants
h = 100  # Initial height in meters
g = 9.8  # Gravitational acceleration in m/s^2 (Earth)

# Create a time array using np.linspace
max_time = np.sqrt(2 * h / g)  # Estimated time to hit the ground
time_steps = 100  # Number of time steps
t = np.linspace(0, max_time, time_steps)

# Calculate the position y at each time step
y = h - (1/2) * g * t**2
y = np.where(y < 0, 0, y)  # Ensure no negative positions

# Calculate the distances fallen between consecutive time steps
distances_fallen = np.diff(y)

# Calculate the average distance fallen
average_distance_fallen = np.mean(distances_fallen)

# Plotting the results
plt.figure(figsize=(14, 8))

# Position vs Time Plot
plt.subplot(2, 2, 1)
plt.plot(t, y, label="Position (y)", color="royalblue")
plt.fill_between(t, y, color="lightblue", alpha=0.3)
plt.title("Position of Ball over Time")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.legend()

# Velocity vs Time Plot (derived from position)
velocity = -g * t  # Since velocity in free fall is v = -g * t
plt.subplot(2, 2, 2)
plt.plot(t, velocity, label="Velocity (v)", color="tomato")
plt.fill_between(t, velocity, color="lightcoral", alpha=0.3)
plt.title("Velocity of Ball over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()

# Distances Fallen between Time Steps
time_midpoints = (t[:-1] + t[1:]) / 2  # Midpoints for plotting distances between steps
plt.subplot(2, 2, 3)
plt.plot(time_midpoints, distances_fallen, label="Distance Fallen per Step", color="green")
plt.title("Distances Fallen per Interval")
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.legend()

# Histogram of Distances Fallen
plt.subplot(2, 2, 4)
plt.hist(distances_fallen, bins=10, color="purple", alpha=0.7)
plt.axvline(average_distance_fallen, color='red', linestyle='dashed', linewidth=2, label=f'Average Distance: {average_distance_fallen:.2f} m')
plt.title("Distribution of Distances Fallen")
plt.xlabel("Distance (m)")
plt.ylabel("Frequency")
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()