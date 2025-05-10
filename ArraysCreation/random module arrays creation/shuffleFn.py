# NumPy random.shuffle() Function

# 1. np.random.shuffle():
#    - Shuffles elements IN-PLACE (modifies the original array directly)
#    - Returns None (doesn't create or return a new array)
#    - Only shuffles the first axis/dimension (rows in a 2D array)
#    - More memory efficient since it doesn't create a copy
#    - Cannot be used with non-array sequences like tuples (they're immutable)
#    - We CANNOT provide a shape parameter as it works on existing arrays
#    - Useful when you want to randomize data without creating extra copies
#    - Perfect for creating random training/test splits or randomizing batches

# Main characteristics:
#    - Works in-place: Modifies the input array directly
#    - Shuffles only along axis 0 (first dimension)
#    - Cannot shuffle along other axes directly without transposing
#    - Returns None, not the shuffled array
#    - Preserves the shape of the original array
#    - Requires a mutable sequence (works with lists and arrays, not tuples)

import numpy as np

# Basic usage with 1D array
array_1d = np.arange(10)
print("Original 1D array:", array_1d)

np.random.shuffle(array_1d)  # Shuffles in-place
print("After shuffle():", array_1d)
print("Return value:", np.random.shuffle(array_1d))  # Shows None

# Using with a list
my_list = [1, 2, 3, 4, 5]
print("\nOriginal list:", my_list)
np.random.shuffle(my_list)
print("List after shuffle():", my_list)

# Working with 2D arrays
array_2d = np.arange(20).reshape(5, 4)
print("\nOriginal 2D array:")
print(array_2d)

np.random.shuffle(array_2d)  # Only shuffles the rows (first dimension)
print("\nAfter shuffle() - notice only rows are shuffled:")
print(array_2d)

# Shuffling columns requires transposing first
array_2d_for_columns = np.arange(20).reshape(5, 4)
print("\nNew 2D array for column shuffling:")
print(array_2d_for_columns)

# Transpose, shuffle, transpose back to shuffle columns
array_2d_for_columns_t = array_2d_for_columns.T  # Transpose
np.random.shuffle(array_2d_for_columns_t)  # Shuffle rows of transposed array
array_2d_for_columns = array_2d_for_columns_t.T  # Transpose back

print("\nAfter column shuffling (transpose + shuffle + transpose):")
print(array_2d_for_columns)

# Common use case: Shuffling multiple arrays in the same way
print("\nShuffling multiple arrays in sync:")
features = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
labels = np.array(['A', 'B', 'C', 'D'])

print("Original features:")
print(features)
print("Original labels:")
print(labels)

# Create an index array and shuffle it
indices = np.arange(len(features))
np.random.shuffle(indices)

# Use the shuffled indices to reorder both arrays
shuffled_features = features[indices]
shuffled_labels = labels[indices]

print("\nShuffled features:")
print(shuffled_features)
print("Shuffled labels (matched with features):")
print(shuffled_labels)

# Important caution: What doesn't work with shuffle
print("\nWhat doesn't work with shuffle:")

try:
    # Trying to shuffle an immutable tuple
    my_tuple = (1, 2, 3, 4, 5)
    print("Original tuple:", my_tuple)
    np.random.shuffle(my_tuple)
except Exception as e:
    print("Error when shuffling tuple:", str(e))

try:
    # Trying to shuffle along a different axis
    array_2d_again = np.arange(20).reshape(5, 4)
    print("\nTrying to shuffle along axis=1 directly:")
    np.random.shuffle(array_2d_again, axis=1)  # This will fail
except Exception as e:
    print("Error:", str(e))
    print("Solution: Use transpose method shown earlier")

# Important note about randomness control
print("\nControlling randomness with seed:")
np.random.seed(42)  # Set seed for reproducibility
array_with_seed = np.arange(10)
np.random.shuffle(array_with_seed)
print("First shuffle with seed 42:", array_with_seed)

np.random.seed(42)  # Reset to same seed
array_with_seed_again = np.arange(10)
np.random.shuffle(array_with_seed_again)
print("Second shuffle with seed 42:", array_with_seed_again)
print("Notice the identical results with the same seed!")