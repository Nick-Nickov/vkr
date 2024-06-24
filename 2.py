from sympy import symbols, Poly

def count_sign_changes(coefficients):
    sign_changes = 0
    prev_sign = coefficients[0] > 0

    for coeff in coefficients[1:]:
        current_sign = coeff > 0
        if current_sign != prev_sign and coeff != 0:
            sign_changes += 1
        prev_sign = current_sign

    return sign_changes

def descartes_rule_of_signs(polynomial):

    x = symbols('x')
    poly = Poly(polynomial, x)
    coeffs = poly.all_coeffs()

    positive_roots = count_sign_changes(coeffs)

    negative_coeffs = [coeff * (-1)**i for i, coeff in enumerate(coeffs)]
    negative_roots = count_sign_changes(negative_coeffs)

    return positive_roots, negative_roots

# Пример использования
x = symbols('x')
polynomial = x**4 - 3*x**3 + 2*x**2 + x - 5

positive_roots, negative_roots = descartes_rule_of_signs(polynomial)
print(f"Количество положительных корней: {positive_roots}")
print(f"Количество отрицательных корней: {negative_roots}")
