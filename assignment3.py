def nth_root(value, n):
    """
    Calculate the nth root of a number.
    
    Args:
        value (float): The number to find the root of.
        n (int): The degree of the root.
        
    Returns:
        float: The nth root of value.
    """
    if n == 0:
        raise ValueError("Cannot calculate the zero root.")
    return value ** (1 / n)

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    
    Args:
        point1 (tuple or list): Coordinates of the first point (x1, y1, ...).
        point2 (tuple or list): Coordinates of the second point (x2, y2, ...).
        
    Returns:
        float: The Euclidean distance between the two points.
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions.")
    
    return sum((a - b) ** 2 for a, b in zip(point1, point2)) ** 0.5

# Example usage:
print("5th root of 32:", nth_root(32, 5))
print("Distance between (1, 2) and (4, 6):", euclidean_distance((1, 2), (4, 6)))
