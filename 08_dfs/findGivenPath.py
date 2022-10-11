class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):

  return explore_all_paths(root, sequence, 0)

def explore_all_paths(root, seq, count):
  if not root:
    return False
  
  if root.val != seq[count]:
    return False
  elif not root.left and not root.right:
    return True
  
  count += 1

  return explore_all_paths(root.left, seq, count) or explore_all_paths(root.right, seq, count)

  


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
