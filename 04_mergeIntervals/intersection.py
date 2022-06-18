def merge(arr_a, arr_b):
  result = []
  p1, p2, start, end = 0, 0, 0, 1

  while p1 < len(arr_a) and p2 < len(arr_b):
    b_overlaps_a = arr_a[p1][start] <= arr_b[p2][start] and arr_a[p1][end] >= arr_b[p2][start]
    a_overlaps_b = arr_b[p2][start] <= arr_a[p1][start] and arr_b[p2][end] >= arr_a[p1][start]

    if (a_overlaps_b or b_overlaps_a):
      result.append([max(arr_a[p1][start], arr_b[p2][start]), 
        min(arr_a[p1][end], arr_b[p2][end])])

    if arr_a[p1][end] < arr_b[p2][end]:
      p1 += 1
    else:
      p2 += 1

  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()