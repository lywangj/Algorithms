from collections import deque


def find_permutations(nums):
  result = []
  generate_subsets(nums, 0, [], result)
  return result

def generate_subsets(nums, index, subset, result):
  if index == len(nums):
    result.append(subset)
    return

  n = len(subset)
  for i in range(n+1):
    tmp = list(subset)
    tmp.insert(i, nums[index])
    generate_subsets(nums, index+1, tmp, result)


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()


# Input: [1,3,5]
# Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]