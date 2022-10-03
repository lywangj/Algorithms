def find_happy_number(num):
  slow, fast = num, num
  assert create_next_number(23) == 13
  while fast != 1:
    slow = create_next_number(slow)
    fast = create_next_number(create_next_number(fast))
    if slow == fast:
      return False
  return True


def create_next_number(num):
  ans = 0
  while num >= 1:
    curr = num % 10
    ans += curr * curr
    num = num // 10
  return ans

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()
