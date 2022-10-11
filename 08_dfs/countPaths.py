class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  return count_paths_recursive(root, S, [])


def count_paths_recursive(currentNode, S, currentPath):

  if not currentNode:
    return 0

  for i in range(len(currentPath)):
    currentPath[i] += currentNode.val
  currentPath.append(currentNode.val)

  if S in currentPath:
    return 1

  return count_paths_recursive(currentNode.left, S, currentPath) \
            + count_paths_recursive(currentNode.right, S, currentPath)
  


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
