def search_next_letter(letters, key):
  n = len(letters)
  l, r = 0, n - 1
  key_num = ord(key)

  while l<= r:
    m = (l + r) // 2
    if ord(letters[m]) < key_num:
      l = m + 1
    elif ord(letters[m]) > key_num:
      r = m - 1
    else:
      return letters[ (m + 1) % (n) ]

  return letters[ l % (n) ]

  

  


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))


main()

# Example 1:

# Input: ['a', 'c', 'f', 'h'], key = 'f'
# Output: 'h'
# Explanation: The smallest letter greater than 'f' is 'h' in the given array.
# Example 2:

# Input: ['a', 'c', 'f', 'h'], key = 'b'
# Output: 'c'
# Explanation: The smallest letter greater than 'b' is 'c'.
# Example 3:

# Input: ['a', 'c', 'f', 'h'], key = 'm'
# Output: 'a'
# Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
# Example 4:

# Input: ['a', 'c', 'f', 'h'], key = 'h'
# Output: 'a'
# Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.