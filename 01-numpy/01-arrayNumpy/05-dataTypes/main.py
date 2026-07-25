# Numpy Data Types

# Numpy data types are:
# - int32, int64
# - unsigned int32, unsigned int64
# - float32, float64
# - complex float64, complex float128
# - bool
# - object
# - string
# - unicode string
# - datetime64
# - timedelta64
# - void

# default data type:
# - int32 for integers
# - float64 for floats
# - complex float128 for complex numbers
# - bool for boolean values
# - string for strings

# Numpy data types can be specified when creating an array using the dtype
# parameter. For example, to create an array of integers with a specific
# data type, you can use the following code:
import numpy as np

# Create an array of integers with a specific data type
int_array: np.ndarray = np.array([1, 2, 3, 4, 5], dtype='i4')
print("Array of integers with specific data type:")
print(int_array)
print(int_array.dtype)  # Output: int32
# i4 means that the array can hold integers of up to 4 bytes (32 bits).

# Create an array of floats with a specific data type
float_array: np.ndarray = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype='f4')
print("\nArray of floats with specific data type:")
print(float_array)
print(float_array.dtype)  # Output: float32
# f4 means that the array can hold floats of up to 4 bytes (32 bits).

# Create an array of complex numbers with a specific data type
complex_array: np.ndarray = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype='c8')
print("\nArray of complex numbers with specific data type:")
print(complex_array)
print(complex_array.dtype)  # Output: complex128
# c8 means that the array can hold complex numbers of up to 8 bytes (64 bits).

# Create an array of boolean values with a specific data type
bool_array: np.ndarray = np.array([True, False, True, False], dtype='bool')
print("\nArray of boolean values with specific data type:")
print(bool_array)
print(bool_array.dtype)  # Output: bool
# bool means that the array can hold boolean values (True or False).

# Create an array of strings with a specific data type
string_array: np.ndarray = np.array(['apple', 'banana', 'cherry'], dtype='S8')
print("\nArray of strings with specific data type:")
print(string_array)
print(string_array.dtype)  # Output: S8
# S8 means that the array can hold strings of up to 8 characters.

# Create an array of unicode strings with a specific data type
unicode_array: np.ndarray = np.array(['apple', 'banana', 'cherry'],
                                     dtype='U6')
print("\nArray of unicode strings with specific data type:")
print(unicode_array)
print(unicode_array.dtype)  # Output: U6
# U6 means that the array can hold unicode strings of up to 6 characters.

# Create an array of datetime values with a specific data type
datetime_array: np.ndarray = np.array(['2022-01-01',
                                       '2022-02-01',
                                       '2022-03-01'],
                                      dtype='M8[D]')
print("\nArray of datetime values with specific data type:")
print(datetime_array)
print(datetime_array.dtype)  # Output: datetime64
# M8[D] means that the array can hold datetime values with a precision of days.
