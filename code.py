"""JUAN CARLO FERREIRA TALLER 3 """


import numpy as np

# Coeficientes de la ecuación cuadrática
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

# Calcula el discriminante
discriminante = b**2 - 4*a*c

if discriminante > 0:
    x1 = (-b + np.sqrt(discriminante)) / (2*a)
    x2 = (-b - np.sqrt(discriminante)) / (2*a)
    print(f"Soluciones reales y diferentes: x1 = {x1}, x2 = {x2}")
elif discriminante == 0:
    x = -b / (2*a)
    print(f"Solución real y doble: x = {x}")
else:
    real = -b / (2*a)
    imag = np.sqrt(abs(discriminante)) / (2*a)
    print(f"Soluciones complejas: x1 = {real}+{imag}j, x2 = {real}-{imag}j")

