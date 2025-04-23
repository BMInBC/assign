def bisection_method(f, a, b, tol=1e-7, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Bisection method requires a sign change in [a, b]")
    
    steps = 0
    while (b - a) / 2.0 > tol and steps < max_iter:
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            break
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        steps += 1
    return steps, (a + b) / 2.0

def newton_raphson_method(f, f_prime, x0, tol=1e-7, max_iter=100):
    steps = 0
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            break
        fpx = f_prime(x)
        if fpx == 0:
            raise ZeroDivisionError("Derivative is zero; no convergence.")
        x = x - fx / fpx
        steps += 1
    return steps, x

def compare_methods(f, f_prime, a, b, x0, tol=1e-7, max_iter=100):
    bisection_steps, bisection_root = bisection_method(f, a, b, tol, max_iter)
    newton_steps, newton_root = newton_raphson_method(f, f_prime, x0, tol, max_iter)

    return {
        "bisection": {"steps": bisection_steps, "root": bisection_root},
        "newton_raphson": {"steps": newton_steps, "root": newton_root}
        
    }


import math

# Function: f(x) = x^3 - x - 2
f = lambda x: x**3 - x - 2
f_prime = lambda x: 3*x**2 - 1

result = compare_methods(f, f_prime, a=1, b=2, x0=1.5)

print("Comparison Result:")
print(result)


