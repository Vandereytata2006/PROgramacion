x0 = float(input("Enter the initial position (m): "))
v0 = float(input("Enter the initial velocity (m/s): "))
a = float(input("Enter the acceleration (m/s²): "))
t = float(input("Enter the time (s): "))

v = v0 + a * t
    
x = x0 + v0 * t + 0.5 * a * t**2
    
print("\nFinal position (x): ", x, "meters")
print("Final velocity (v): ", v, "m/s")
print("Acceleration (a): ", a, "m/s²")