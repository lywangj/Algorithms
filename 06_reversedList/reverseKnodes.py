from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, k):
  if k ==0 :
    return head

  last_node_in_first_part = head

  prev, curr, next = None, head, None

  for _ in range(k):
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

#   head = prev
  last_node_in_first_part.next = curr

  return prev
  


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
