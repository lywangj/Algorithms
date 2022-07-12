# Number Range (medium)  # do it again

def find_range(arr, key):
  left, right = 0, len(arr)
  result = [-1, -1]

  result[0] = binary_search(arr, key, left, right, 0)
  if result[0] != -1:
    result[1] = binary_search(arr, key, left, right, 1)
  return result


def binary_search(arr, key, left, right, findMax):
  keyIndex = -1
  while left <= right:
    mid = left + (right - left) // 2
    if key < arr[mid]:
      right = mid - 1
    elif key > arr[mid]:
      left = mid + 1
    else:
      keyIndex = mid
      if findMax:
        left = mid + 1
      else:
        right = mid - 1
  return keyIndex


def main():
  print(find_range([4, 6, 6, 6, 9], 6))         # [1, 3]
  print(find_range([1, 3, 8, 10, 15], 10))      # [3, 3]
  print(find_range([1, 3, 8, 10, 15], 12))      # [-1, -1]

main()
