import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):
  # find the proper bounds first

  return binary_search(reader, key, 0, 50)


def binary_search(reader, key, l, r):

  while l <= r:
    m = (l + r) // 2
    if reader.get(m) == math.inf:
      r = m - 1
    elif reader.get(m) < key:
      l = m + 1
    elif reader.get(m) > key:
      r = m - 1
    else:
      return m

  return -1


def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()


# Example 1:

# Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
# Output: 6
# Explanation: The key is present at index '6' in the array.

# Example 2:

# Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
# Output: -1
# Explanation: The key is not present in the array.

# Example 3:

# Input: [1, 3, 8, 10, 15], key = 15
# Output: 4
# Explanation: The key is present at index '4' in the array.

# Example 4:

# Input: [1, 3, 8, 10, 15], key = 200
# Output: -1
# Explanation: The key is not present in the array.