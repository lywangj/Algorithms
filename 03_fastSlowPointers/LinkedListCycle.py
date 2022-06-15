from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  cycle_length = 0
  # setup one fast pointer & one slow pointer #
  slow, fast = head, head
  # moving two pointers forward #
  # until they point to the same node due to cycle #
  while (fast is not None and fast.next is not None):
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      cycle_length = calculate_cycle_length(slow)
      break
  return find_start(head, cycle_length)


def calculate_cycle_length(slow):
  # count n, the number of nodes in cycle #
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length


def find_start(head, cycle_length):
  # move fast pointer nth-node ahead of slow pointer
  slow = head
  fast = head
  while cycle_length > 0:
    fast = fast.next
    cycle_length -= 1
  # when slow pointer catch up fast pointer #
  # Their meeting point will be the start of the cycle #
  while slow != fast:
    slow = slow.next
    fast = fast.next
  return slow


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()