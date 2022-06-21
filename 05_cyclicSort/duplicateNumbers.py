def find_all_duplicates(nums):
  duplicateNumbers = []
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      # swap  
      nums[i], nums[j] = nums[j], nums[i]  
    else: 
      # find duplicate number, but in wrong position
      if nums[i] != i+1:
        duplicateNumbers.append(nums[i])
      i += 1

  return duplicateNumbers


def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))


main()
