import math

# Define the function f(x)
def f(x):
    return 4 * x + math.sin(x) - math.exp(x)

# Define the derivative f'(x)
def df(x):
    return 4 + math.cos(x) - math.exp(x)

# Newton-Raphson Method Implementation
def newton_raphson(x0, tol=1e-5, max_iter=100):
    print("iter.\txk\t\t\tf(xk)\t\t\tError")
    for k in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print("Zero derivative. No solution found.")
            return None

        x1 = x0 - fx / dfx
        err = abs((x1 - x0) / x1)

        print(f"{k}\t{x1:.16f}\t{f(x1):.16f}\t{err:.12f}")

        if err < tol:
            print("Required accuracy achieved; Solution is convergent.")
            return x1

        x0 = x1

    print("The number of iterations exceeded the maximum limit.")
    return None

# Use initial approximation x0 = 0 (as given in the example)
initial_guess = 0.0
solution = newton_raphson(initial_guess)





