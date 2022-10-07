def find_all_duplicates(nums):
  dulplicate_numbers = []
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  for k in range(len(nums)):
    if nums[k] != k + 1:
      dulplicate_numbers.append(nums[k])

  return dulplicate_numbers



def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
