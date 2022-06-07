def non_repeat_substring(str1):
  start_point = 0
  max_length = 0
  char_index_map = {}

  for end_point in range(len(str1)):
    right_char = str1[end_point]
    if right_char in char_index_map:
      start_point = max(start_point, char_index_map[right_char] + 1)
    char_index_map[right_char] = end_point
    max_length = max(max_length, end_point - start_point + 1)
  return max_length


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
  print("Length of the longest substring: " + str(non_repeat_substring("bbabcabcdd")))


main()