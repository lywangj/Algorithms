def remove_duplicates(arr):
  slow, fast = 0, 1
  count = 1
  while fast < len(arr):
    if arr[slow] != arr[fast]:
      count += 1
      slow = fast
    fast += 1
  return count

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))

main()
