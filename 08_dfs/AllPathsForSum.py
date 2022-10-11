class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, required_sum):
  paths = []
#   curr_path = []

  explore_paths(root, required_sum, [], paths)

  return paths

def explore_paths(root, required_sum, curr_path, paths):
  if root is None:
    # curr_path = curr_path[:-2]
    return

  curr_path.append(root.val)

  if root.val == required_sum and not root.left and not root.right:
    paths.append(list(curr_path))
  else:
    explore_paths(root.left, required_sum - root.val, curr_path, paths)
    explore_paths(root.right, required_sum - root.val, curr_path, paths)

  del curr_path[-1]
  


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(find_paths(root, required_sum)))


main()
