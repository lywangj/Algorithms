from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root is None:
    return None
  find_target = False
  q = deque()
  q.append(root)
  while q:
    level_size = len(q)

    for _ in range(level_size):
      curr_node = q.popleft()
      if find_target:
        return curr_node
      if curr_node.val == key:
        find_target = True
      if curr_node.left: q.append(curr_node.left)
      if curr_node.right: q.append(curr_node.right)

  return None


def main():
  
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);
  
  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = find_successor(root, 9)
  if result:
    print(result.val)
  
  result = find_successor(root, 12)
  if result:
    print(result.val)


main()
