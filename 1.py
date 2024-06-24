import numpy as np
from sympy import symbols, Poly

def sturm_sequence(polynomial):
    x = symbols('x')
    poly = Poly(polynomial, x)
    sturm_seq = [poly, poly.diff(x)]
    
    while True:
        remainder = -sturm_seq[-2].rem(sturm_seq[-1])
        if remainder == 0:
            break
        sturm_seq.append(remainder)
    
    return sturm_seq

def sign_changes(seq, val):
    signs = [poly.eval(val).evalf() for poly in seq]
    signs = [s > 0 for s in signs]
    
    changes = 0
    for i in range(1, len(signs)):
        if signs[i] != signs[i-1]:
            changes += 1
            
    return changes

def count_real_roots(polynomial, a, b):
    sturm_seq = sturm_sequence(polynomial)
    
    v_a = sign_changes(sturm_seq, a)
    v_b = sign_changes(sturm_seq, b)
    
    return v_a - v_b

x = symbols('x')
polynomials = [
    x**4 - 3*x**3 + 2*x**2 + x - 5,
]

a, b = -10, 10

results = [count_real_roots(p, a, b) for p in polynomials]
print(results)
