def remove_element(arr, key):
  slow, fast = 0, 0
  while fast < len(arr):
    if arr[fast] != key:
      arr[slow] = arr[fast]
      slow += 1
    fast += 1
  print (arr[:slow])
  return slow


def main():
  print("Array new length: " +
        str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
  print("Array new length: " +
        str(remove_element([2, 11, 2, 2, 1], 2)))


main()
