def search_triplets(arr):
  arr.sort()
  triples = []
  for i in range(len(arr)):
    # curr_triple.append(i)
    search_pairs(arr, i, -1 * arr[i], triples)
  return triples

def search_pairs(arr, index, target, triples):
  left, right = index + 1, len(arr) - 1
  while left < right:
    curr_sum = arr[left] + arr[right]
    if curr_sum == target:
      tmp = [arr[index], arr[left], arr[right]]
      triples.append(tmp)
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left-1]:
        left += 1
      while left < right and arr[right] == arr[right+1]:
        right -= 1
    elif curr_sum < target:
      left += 1
    else:
      right -= 1


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))
  print(search_triplets([-3, 0, 1, 2, -1, 1, 1, 1, -2]))

main()
