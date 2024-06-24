import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Poly, solve, lambdify

def plot_polynomial_and_roots(polynomial, a, b):
    x = symbols('x')
    poly = Poly(polynomial, x)
    f = lambdify(x, poly.as_expr(), 'numpy')
    
    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Многочлен')
    
    roots = solve(polynomial, x)
    real_roots = [r.evalf() for r in roots if r.is_real]
    
    for root in real_roots:
        plt.plot(root, 0, 'ro')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('График многочлена и его корни')
    plt.legend()
    plt.grid(True)
    plt.show()

    return real_roots

x = symbols('x')
polynomials = [
    x**5 - 5*x**3 - 1
]

intervals = [
    (-3, 4)
]

results = {}
for poly, interval in zip(polynomials, intervals):
    print(f"График для многочлена: {poly}")
    roots = plot_polynomial_and_roots(poly, *interval)
    results[str(poly)] = roots
    print(f"Вещественные корни: {roots}")

results
