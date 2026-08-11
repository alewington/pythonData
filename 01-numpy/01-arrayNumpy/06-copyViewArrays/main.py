# what is the difference between a copy and a view of an array in NumPy?

# A copy of an array is a new array that contains the same data as the
# original array but is stored in a different memory location. Changes made
# to the copy do not affect the original array, and vice versa.

# A view of an array, on the other hand, is a new array that shares the same
# data as the original array but is stored in a different memory location.
# Changes made to the view will affect the original array, and vice versa.

# In summary, a copy creates a new array with its own data, while a view
# creates a new array that shares the same data as the original array.

# When should you use a copy vs a view?

# You should use a copy when you want to create a new array that is independent
# of the original array and you want to make changes to the new array without
# affecting the original array.
# example that is easy to understand is when you want to create a new array
# that is a modified version of the original array, but you want to keep the
# original array unchanged. Like testing to see if a new method of teaching is
# effective for a specific year group of students, but you want to keep the
# original data for comparison.

# You should use a view when you want to create a new array that shares the
# same data as the original array and you want to make changes to the new array
# that will also affect the original array.
# Example that is easy to understand is when you want to create a new array
# that extracts a subset of the original array, but you want to update the
# original array when you make changes.
# like updating student information for a specific year group
