from re import M


def binary_search(arr, key):
  n = len(arr)
  non_decreasing = False
  if arr[0] < arr[n - 1]:
    non_decreasing = True
  l, r = 0, n - 1

  while l <= r:
    m = (l + r) // 2
    if arr[m] == key:
      return m
    elif arr[m] < key and non_decreasing:
      l = m + 1
    elif arr[m] < key:
      r = m - 1
    elif arr[m] > key and non_decreasing:
      r = m - 1
    else:
      l = m + 1

  return -1
  


def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()

# Example 1:

# Input: [4, 6, 10], key = 10
# Output: 2

# Example 2:

# Input: [1, 2, 3, 4, 5, 6, 7], key = 5
# Output: 4

# Example 3:

# Input: [10, 6, 4], key = 10
# Output: 0

# Example 4:

# Input: [10, 6, 4], key = 4
# Output: 2