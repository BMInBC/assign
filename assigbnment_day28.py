import matplotlib.pyplot as plt

# Generate numbers from 1 to 1000
numbers = list(range(1, 1001))
squares = [x**2 for x in numbers]

# Create a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(numbers, squares, color='blue', s=10)
plt.title("Square of Numbers from 1 to 1000")
plt.xlabel("Number")
plt.ylabel("Square")
plt.grid(True)
plt.tight_layout()
plt.show()
