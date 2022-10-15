def search_min_diff_element(arr, key):

  n = len(arr)
  
  if key < arr[0]:
    return arr[0]
  elif key > arr[n - 1]:
    return arr[n - 1]

  l, r = 0, n - 1
  while l <= r:
    m = (l + r) // 2
    if arr[m] < key:
      l = m + 1
    elif arr[m] > key:
      r = m - 1
    else:
      return arr[m]

  if abs(arr[l] - key) < abs(arr[r] - key):
    return arr[l]
  else:
    return arr[r]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()


# Example 1:

# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

# Example 2:

# Input: [4, 6, 10], key = 4
# Output: 4

# Example 3:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: 10

# Example 4:

# Input: [4, 6, 10], key = 17
# Output: 10