def make_squares(arr):
  left, right = 0, len(arr) - 1
  while left < right:
    left_square = arr[left] * arr[left]
    right_square = arr[right] * arr [right]
    if left_square < right_square:
      arr[right] = right_square
    else:
      arr[left] = arr[right]
      arr[right] = left_square
    right -= 1
  return arr


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
