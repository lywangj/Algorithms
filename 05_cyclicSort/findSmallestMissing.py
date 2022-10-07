def find_first_smallest_missing_positive(nums):
  i = 0
  n = len(nums)
  while i < n :
    j = nums[i] - 1
    if n >= nums[i] > 0 and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  for k in range(n):
    if nums[k] != k + 1:
      return k + 1
       


def main():
  print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()
