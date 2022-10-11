class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root):
  paths = []

  explore_all_paths(root, [], paths)

  return paths

def explore_all_paths(root, curr_path, paths):
  
  curr_path.append(root.val)

  if not root.left and not root.right:
    paths.append(list(curr_path))
    
  if root.left: explore_all_paths(root.left, curr_path, paths)
  if root.right: explore_all_paths(root.right, curr_path, paths)

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
        ": " + str(find_paths(root)))


main()
