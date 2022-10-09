from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  results = []
  q = deque()
  q.append(root)

  while q:

    level_size = len(q)
    level = []

    for _ in range(level_size):

      curr = q.popleft()
      level.append(curr.val)

      if curr.left is not None:
        q.append(curr.left)
      if curr.right is not None:
        q.append(curr.right)

    results.append(level)

  return results


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
