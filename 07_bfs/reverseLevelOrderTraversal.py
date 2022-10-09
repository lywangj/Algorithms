from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  results = deque()
  q = deque()
  q.append(root)

  while q:
    
    level_size = len(q)
    level = []
    for _ in range(level_size):
      curr_node = q.popleft()
      level.append(curr_node.val)

      if curr_node.left is not None:
        q.append(curr_node.left)
      if curr_node.right is not None:
        q.append(curr_node.right)

    results.appendleft(level)

  return results



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
