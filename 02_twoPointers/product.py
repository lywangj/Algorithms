from collections import deque


def find_subarrays(arr, target):
  subarrays = []
  for i in range(len(arr)):
    if arr[i] <= target:
      curr_target = target / arr[i]
      curr_subarr = []
      curr_subarr.append(arr[i])
      subarrays.append(list(curr_subarr))
      for j in range(i+1, len(arr)):
        if arr[j] <= curr_target:
          curr_subarr.append(arr[j])
          subarrays.append(list(curr_subarr))
          curr_target /= arr[j]
  return subarrays

def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 1, 1, 6, 5], 50))


main()
