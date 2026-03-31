import math

def roots(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        r1 = (-b + math.sqrt(discriminante)) / (2*a)
        r2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminante == 0:
        r = (-b) / (2*a)
        return f"({r})"
    else:
        return "( )"


def value_y(a, b, c, x):
    return a*x**2 + b*x + c


def to_string(a, b, c):
    if a != 0:
        if b != 0:
            return f"f(x) = {a} * X^2 + {b} * X + {c}"
        else:
            return f"f(x) = {a} * X^2 + {c}"
    else:
        if b != 0:
            return f"f(x) = {b} * X + {c}"
        else:
            return f"f(x) = {c}"


def derivation(a, b, c):
    deriv_a = 2 * a
    deriv_b = b

    if deriv_a != 0:
        if deriv_b != 0:
            return f"f'(x) = {deriv_a} * X + {deriv_b}"
        else:
            return f"f'(x) = {deriv_a} * X"
    else:
        if deriv_b != 0:
            return f"f'(x) = {deriv_b}"
        else:
            return f"f'(x) = 0"
