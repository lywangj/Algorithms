### Level Averages in a Binary Tree

Given a binary tree, create an array to record the averages of all of its levels.

- tree: [1] -> [2, 3] -> [4, 5, null, 7]
- avg: [1, 2.5, 5.3]

Task:
- With breadth-first search, calcute the averages of each level.

Time complexity: O(n)
- n as the total number of nodes in the tree

Space complexity: O(n)
- n as the total number of nodes in the tree. The maximum space will be the half of n.

Constraints:
- 1 <= tree.level <= 100
- 1 <= treeNode.value <= 1000