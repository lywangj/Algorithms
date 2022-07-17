# Single Number (easy)

def find_single_number(arr):
  x = arr[0]
  for i in range(1, len(arr)):
    x = x ^ arr[i]
  return x
  

def main():
  arr = [1, 4, 2, 1, 3, 2, 3]
  print(find_single_number(arr))      # 4
  arr1 = [7, 9, 7]
  print(find_single_number(arr1))     # 9

main()

# Input: 1, 4, 2, 1, 3, 2, 3
# Output: 4

# Input: 7, 9, 7
# Output: 9