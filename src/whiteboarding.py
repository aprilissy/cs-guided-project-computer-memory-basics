# Zeros to the Right
# Write a function that takes an array of integers and moves each non-zero integer to the left side of the array. The function should return the mutated array. The order of the non-zero integers does not matter in the mutated array.
# Examples
# Sample input: [0, 3, 1, 0, -2]
# Expected output: [3, 1, -2, 0, 0]
# Sample input: [4, 2, 1, 5]
# Expected output: [4, 2, 1, 5]

def zeros_to_the_right(num_array):
  try:
    num_array.index(0)
    sort = num_array.sort(reverse=True)
    while num_array[-1] != 0:
      num_array = num_array[-1:] + num_array[:-1]
    return num_array
  except:
    return num_array

print(zeros_to_the_right([0, 3, 1, 0, -2]))
print(zeros_to_the_right([4, 2, 1, 5]))
print(zeros_to_the_right([0, 3, 1, 0, -2, -1, -5]))
