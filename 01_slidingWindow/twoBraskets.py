def fruits_into_baskets(fruits):
  window_st, window_end = 0, 0
  baskets = {}
  max_length = 0
  for window_end in range(0, len(fruits)):
    if fruits[window_end] not in baskets:
        baskets[fruits[window_end]] = 0
    baskets[fruits[window_end]] += 1
    while len(baskets) > 2:
      baskets[fruits[window_st]] -= 1
      if baskets[fruits[window_st]] == 0:
        del baskets[fruits[window_st]]
      window_st += 1

    max_length = max(max_length, window_end-window_st+1)
  
  return max_length

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
