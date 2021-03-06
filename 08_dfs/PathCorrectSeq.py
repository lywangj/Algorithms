from ast import Not


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    return search(root, sequence, 0)


def search(root, sequence, index):
    if root is None:
        return False

    seqLen = len(sequence)
    if index >= seqLen or root.val != sequence[index]:
        return False

    if root.left is None and root.right is None and index == seqLen - 1:
        return True
    
    return search(root.left, sequence, index + 1) or search(root.right, sequence, index + 1)


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
  print("Tree has path sequence: " + str(find_path(root, [0, 1, 6])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1])))


main()
