from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  minimum_depth = 0
  if root is None:
    return 0
  q = deque()
  q.append(root)

  while q:
    minimum_depth += 1
    level_size = len(q)

    for _ in range(level_size):
      curr_node = q.popleft()
      if curr_node.left is None and curr_node.right is None:
        return minimum_depth
      if curr_node.left is not None:
        q.append(curr_node.left)
      if curr_node.right is not None:
        q.append(curr_node.right)



def main():
  root = TreeNode(12)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
