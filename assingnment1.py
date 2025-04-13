import time
import matplotlib.pyplot as plt
import math

def cube_root(n):
    """
    Finds cube root of integer n using binary search.
    Returns cube root, steps taken, and time used.
    """
    is_negative = n < 0
    n = abs(n)
    
    if n == 0 or n == 1:
        return (-n if is_negative else n), 0, 0

    start = 0
    end = n
    steps = 0
    start_time = time.time()

    while start <= end:
        steps += 1
        mid = (start + end) // 2
        mid_cubed = mid ** 3

        if mid_cubed == n:
            root = mid
            break
        elif mid_cubed < n:
            start = mid + 1
            root = mid  # floor value
        else:
            end = mid - 1

    end_time = time.time()
    root = -root if is_negative else root
    return root, steps, end_time - start_time

# Graphing: Steps vs Digits
digits_list = list(range(1, 16))
step_counts = []
times = []

for d in digits_list:
    num = 10**d - 1
    _, steps, t = cube_root(num)
    step_counts.append(steps)
    times.append(t)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(digits_list, step_counts, marker='o')
plt.title("Steps vs Digits")
plt.xlabel("Number of Digits")
plt.ylabel("Steps")

plt.subplot(1, 2, 2)
plt.plot(digits_list, times, marker='s', color='green')
plt.title("Python Execution Time vs Digits")
plt.xlabel("Number of Digits")
plt.ylabel("Time (s)")

plt.tight_layout()
plt.show()
