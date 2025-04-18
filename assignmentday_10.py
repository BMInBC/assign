def find_root(x, tolerance=1e-7):
    low = 0
    high = max(1.0, x)
    guess = (low + high) / 2.0

    while abs(guess**3 - x) > tolerance:
        if guess**3 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0

    return guess