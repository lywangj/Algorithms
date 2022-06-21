using namespace std;

#include <iostream>
#include <vector>

class FindAllDuplicate {
 public:
  static vector<int> findNumbers(vector<int> &nums) {
    vector<int> duplicateNumbers;
    for(int i=0;i<nums.size();) {
      if(nums[i]!=nums[nums[i]-1]){
        swap(nums[i],nums[nums[i]-1]);
      }else{
        if(nums[i]!=i+1){
          duplicateNumbers.push_back(nums[i]);
        }
        ++i;
      }
    }
    return duplicateNumbers;
  }
};

int main(int argc, char *argv[]) {
  vector<int> v1 = {3, 4, 4, 5, 5};
  vector<int> duplicates = FindAllDuplicate::findNumbers(v1);
  cout << "Duplicates are: ";
  for (auto num : duplicates) {
    cout << num << " ";
  }
  cout << endl;
}