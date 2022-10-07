def find_corrupt_numbers(nums):
  pair = []
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  for k in range(n):
    if nums[k] != k + 1:
      return [nums[k], k + 1]


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()
