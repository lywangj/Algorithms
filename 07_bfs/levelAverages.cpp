using namespace std;

#include <iostream>
#include <queue>

class TreeNode {
 public:
  int val = 0;
  TreeNode *left;
  TreeNode *right;

  TreeNode(int x) {
    val = x;
    left = right = nullptr;
  }
};

class LevelAverage {
 public:
  static vector<double> findLevelAverages(TreeNode *root) {
    vector<double> result;
    if (root == nullptr) {
      return result;
    }

    queue<TreeNode *> q;
    q.push(root);
    while(!q.empty()) {
      int size=q.size();
      int levelSum=0;
      for(int i=0;i<size;++i) {
        TreeNode *currNode=q.front();
        q.pop();
        // add the current node's value 
        levelSum+=currNode->val;

        // store the nodes in the next level to queue
        if(currNode->left!=nullptr) {
          q.push(currNode->left);
        }
        if(currNode->right!=nullptr) {
          q.push(currNode->right);
        }
      }
      // append the current level's average to the result array
      result.push_back((double)levelSum/size);
    }

    return result;
  }
};

int main(int argc, char *argv[]) {
  TreeNode *root = new TreeNode(1);
  root->left = new TreeNode(2);
  root->right = new TreeNode(3);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(5);
  root->right->right = new TreeNode(7);
  vector<double> result = LevelAverage::findLevelAverages(root);
  cout << "Level averages are: ";
  for (auto num : result) {
    cout << num << " ";
  }
}
