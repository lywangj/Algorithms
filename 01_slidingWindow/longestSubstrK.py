def longest_substring_with_k_distinct(str1, k):
  window_st, window_end = 0, 0
  max_length = 0
#   dictionary = [0 for x in range(26)]
  store = {}
  for window_end in range(0, len(str1)):
    # dictionary[ord(str1[window_end])] = 1
    if str1[window_end] not in store:
      store[str1[window_end]] = 0
    store[str1[window_end]] += 1
    while len(store) > k:
      max_length = max(max_length, window_end - window_st)
      store[str1[window_st]] -= 1
      if store[str1[window_st]] == 0:
        del store[str1[window_st]]
      window_st += 1

  return max_length

# "araaci", 2 => 4

def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
