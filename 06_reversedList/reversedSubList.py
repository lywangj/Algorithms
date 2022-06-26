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


def reverse_sub_list(head, p, q):
  if p == q:
    return head

  # Skipping 'p-1' nodes, move current pointer to 'p'th node
  curr, prev = head, None
  i = 0
  while curr is not None and i < p - 1:
    prev = curr
    curr = curr.next
    i += 1

  # set a mark pointing to the node at index 'p-1'
  last_node_of_first_part = prev
  # set a mark pointing to the node at index 'p' 
  # that will be the last node of reversed sub list.
  last_node_of_sub_list = curr

  # reverse nodes between 'p' and 'q'
  next = None
  i = 0
  while curr is not None and i < q - p + 1:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    i += 1

  # connect first part to reversed sub list
  if last_node_of_first_part is not None:
    # 'prev' is now the first node of the sub-list
    last_node_of_first_part.next = prev
  else:
    head = prev

  # connect with the last part
  # 'curr' is now the first node of the last part
  last_node_of_sub_list.next = curr
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()