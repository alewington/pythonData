# Logarithms using NumPy Universal Functions (ufuncs)

# NumPy provides a set of universal functions (ufuncs) that allow you to
# perform element-wise operations on arrays. These functions are optimised
# for performance and can handle broadcasting, which allows you to perform
# operations on arrays of different shapes.

import numpy as np

# Create a 1-dimensional array with positive values
arr = np.array([1, 10, 100, 1000, 10000])

# Calculate the natural logarithm (base e) of the elements in the array
natural_log = np.log(arr)
print("Natural Logarithm (base e):", natural_log)

# Calculate the logarithm base 10 of the elements in the array
log_base_10 = np.log10(arr)
print("Logarithm Base 10:", log_base_10)

# Calculate the logarithm base 2 of the elements in the array
log_base_2 = np.log2(arr)
print("Logarithm Base 2:", log_base_2)

# You can also use the shorthand methods for logarithms
natural_log_shorthand = np.log(arr)
log_base_10_shorthand = np.log10(arr)
log_base_2_shorthand = np.log2(arr)
print("Natural Logarithm (shorthand, base e):", natural_log_shorthand)
print("Logarithm Base 10 (shorthand):", log_base_10_shorthand)
print("Logarithm Base 2 (shorthand):", log_base_2_shorthand)

# These operations are performed element-wise, meaning that each element in
# the array is transformed according to the specified logarithmic function.
# You can log() negative numbers or zero, but it will result in
# NaN (Not a Number) or -inf (negative infinity) values, as logarithms are
# undefined for these inputs.

# logarithms are mathematical functions that are the inverse of exponentiation.
# They are used to solve equations involving exponential growth or decay, and
# they have applications in various fields such as science, engineering,
# and finance. They are used alot with calculating the time complexity of
# algorithms, especially in computer science and data analysis.

# for example, the logarithm base 2 is commonly used to analyze the
# performance of algorithms that divide a problem in half at each step,
# such as binary search or merge sort. This would look like log2(n) where n is
# the size of the input data. The logarithm base 10 is commonly used in
# scientific notation and to analyze algorithms with decimal scaling.

# Python example for calculating a binary search time complexity using
# logarithm base 2:


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage of the binary_search function
arr = np.array([1, 10, 100, 1000, 10000])
target = 1000
index = binary_search(arr, target)

print(f"Target {target} found at index: {index}")
print(f"Time complexity of binary search for array of size {len(arr)}:",
      f"O(log2({len(arr)}))")

# base 2 - binary
print(f"Calculated logarithm base 2 of array size: {np.log2(len(arr))}")
print(f"Calculated logarithm base 2 of target value {target}:",
      f"{np.log2(target)}")

# base 10 - denary / decimal
print(f"Calculated logarithm base 10 of array size: {np.log10(len(arr))}")
print(f"Calculated logarithm base 10 of target value {target}:",
      f"{np.log10(target)}")

# base e - natural (Euler's number ~ 2.71828)
print("Calculated natural logarithm (base e) of array size:",
      f"{np.log(len(arr))}")
print(f"Calculated natural logarithm (base e) of target value {target}:",
      f"{np.log(target)}")

# The time complexity of the binary search algorithm is O(log2(n)), where n is
# the size of the input array. This means that as the size of the input array
# increases, the number of comparisons needed to find the target value grows
# logarithmically, making binary search an efficient algorithm for searching
# in sorted arrays.
