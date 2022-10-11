class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  return explore_all_paths(root, 0)

def explore_all_paths(root, sum):
  if not root:
    return 0

  sum += root.val
  
  if not root.left and not root.right:
    return sum

  return explore_all_paths(root.left, sum * 10) + explore_all_paths(root.right, sum * 10)

  

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
