# Import necessary libraries
import random  # For generating random numbers
import math    # For math operations (like square root)
import time    # For measuring execution time
from heapq import heappop, heappush  # For heap operations

# =============================================
# 1. GENERATE SENSOR DATA
# =============================================

# Create 1000 random numbers between 0 and 100 to simulate sensor readings
# Each number represents a sensor measurement (like temperature or pressure)
sensor_data = [random.uniform(0, 100) for _ in range(1000)]

# Choose a target value to search for (we pick the 500th element)
target_value = sensor_data[500]  

# Create a sorted version of the data for algorithms that need sorted input
sorted_data = sorted(sensor_data.copy())  

# =============================================
# 2. SEARCHING ALGORITHMS
# =============================================

def linear_search(arr, target):
    """
    Simplest search - checks each item one by one
    Works on any list (sorted or unsorted)
    """
    for i, val in enumerate(arr):  # Go through each value
        if val == target:          # If we find the target
            return i               # Return its position
    return -1  # Return -1 if not found

def binary_search(arr, target):
    """
    Fast search for SORTED lists only
    Cuts the search area in half each time
    """
    low, high = 0, len(arr) - 1  # Start with full range
    
    while low <= high:
        mid = (low + high) // 2   # Check middle point
        
        if arr[mid] < target:     # If target is in right half
            low = mid + 1
        elif arr[mid] > target:   # If target is in left half
            high = mid - 1
        else:
            return mid            # Found it!
    return -1  # Not found

def jump_search(arr, target):
    """
    Jump through list in blocks, then do linear search in correct block
    Needs sorted data
    """
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0
    
    # Jump ahead until we pass the target
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Not found
    
    # Linear search in the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

def interpolation_search(arr, target):
    """
    Smart search that guesses position based on value distribution
    Works best on uniformly distributed sorted data
    """
    low, high = 0, len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        # Calculate probable position
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# =============================================
# 3. SORTING ALGORITHMS
# =============================================

def bubble_sort(arr):
    """
    Simplest sort - compares neighbors and swaps if wrong order
    Very slow for large lists
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    return arr

def selection_sort(arr):
    """
    Finds minimum element and puts it in correct position
    """
    for i in range(len(arr)):
        min_idx = i  # Assume current position is minimum
        
        # Check rest of list for smaller values
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum with current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """
    Builds final sorted array one item at a time
    Good for small or nearly sorted lists
    """
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to place
        j = i-1
        
        # Move elements that are greater than key
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key  # Insert in correct position
    return arr

def merge_sort(arr):
    """
    Divide and conquer algorithm - splits list in halves recursively
    Very efficient for large lists
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find middle
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half
        
        # Recursively sort both halves
        merge_sort(L)
        merge_sort(R)
        
        # Merge the sorted halves
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Copy any remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    """
    Fastest general-purpose sort in practice
    Picks a pivot and partitions the list
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    """
    Uses binary heap structure to sort
    Always runs in O(n log n) time
    """
    heap = []
    # Build the heap
    for value in arr:
        heappush(heap, value)
    # Extract elements in order
    return [heappop(heap) for _ in range(len(heap))]

# =============================================
# 4. TESTING THE ALGORITHMS
# =============================================

print("\n=== SEARCHING ALGORITHMS ===")

# Test Linear Search
start = time.time()
result = linear_search(sensor_data, target_value)
print(f"Linear Search: Found at index {result} in {time.time()-start:.6f}s")

# Test Binary Search (needs sorted data)
start = time.time()
result = binary_search(sorted_data, target_value)
print(f"Binary Search: Found at index {result} in {time.time()-start:.6f}s")

# Test Jump Search (needs sorted data)
start = time.time()
result = jump_search(sorted_data, target_value)
print(f"Jump Search: Found at index {result} in {time.time()-start:.6f}s")

# Test Interpolation Search (needs sorted data)
start = time.time()
result = interpolation_search(sorted_data, target_value)
print(f"Interpolation Search: Found at index {result} in {time.time()-start:.6f}s")

print("\n=== SORTING ALGORITHMS ===")

# Make copies of original data for sorting tests
test_data = sensor_data.copy()
start = time.time()
bubble_sort(test_data)
print(f"Bubble Sort completed in {time.time()-start:.6f}s")

test_data = sensor_data.copy()
start = time.time()
selection_sort(test_data)
print(f"Selection Sort completed in {time.time()-start:.6f}s")

test_data = sensor_data.copy()
start = time.time()
insertion_sort(test_data)
print(f"Insertion Sort completed in {time.time()-start:.6f}s")

test_data = sensor_data.copy()
start = time.time()
merge_sort(test_data)
print(f"Merge Sort completed in {time.time()-start:.6f}s")

test_data = sensor_data.copy()
start = time.time()
quick_sort(test_data)
print(f"Quick Sort completed in {time.time()-start:.6f}s")

test_data = sensor_data.copy()
start = time.time()
heap_sort(test_data)
print(f"Heap Sort completed in {time.time()-start:.6f}s")