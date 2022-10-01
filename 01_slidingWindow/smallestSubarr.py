import math
# answer
def smallest_subarray_sum(s, arr):
  
  min_length = math.inf
  window_sum = 0
  window_start = 0
  for window_end in range(0, len(arr)):
      window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
      while window_sum >= s:
        min_length = min(min_length, window_end - window_start + 1)
        window_sum -= arr[window_start]
        window_start += 1
      
  if min_length == math.inf:
    return 0
  return min_length

  
# my code
def smallest_subarray_sum(s, arr):
  window_st, window_end = 0, 0
  arr_len = len(arr)
  smallest_len = arr_len + 1
  sum = 0
  while window_end < arr_len:
    sum += arr[window_end]
    while sum >= s:
      smallest_len = min(smallest_len, window_end-window_st+1)
      sum -= arr[window_st]
      window_st += 1
    window_end += 1

  if smallest_len == arr_len + 1:
    return 0
  return smallest_len


def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()
