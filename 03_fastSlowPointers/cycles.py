class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:  # found the cycle
    #   return 3
      return calculate_cycle_length(slow)
  return 0

def calculate_cycle_length(slow):
  count = 1
  current = slow.next
  while current != slow:
    current = current.next
    count += 1
  return count

def find_cycle_start(head, cycle_length):
  fast2 = head
  for _ in range(cycle_length):
    fast2 = fast2.next
  cycle_start = head
  while fast2 != cycle_start:
    fast2 = fast2.next
    cycle_start = cycle_start.next
  return cycle_start

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
