from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  results = []
  q = deque()
  q.append(root)
  order = 1

  while q:
    level_size = len(q)
    curr_level = deque()

    for _ in range(level_size):
      curr_node = q.popleft()
      if order % 2 != 0:
        curr_level.append(curr_node.val)
      else:
        curr_level.appendleft(curr_node.val)

      if curr_node.left is not None:
        q.append(curr_node.left)
      if curr_node.right is not None:
        q.append(curr_node.right)
    
    order += 1
    results.append(list(curr_level))
    
  return results


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
