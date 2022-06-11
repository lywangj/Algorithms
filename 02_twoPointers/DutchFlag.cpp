using namespace std;

#include <iostream>
#include <vector>

class DutchFlag {
 public:
  static void sort(vector<int> &arr) {
    // TODO: Write your code here   
    int low=0, high=arr.size()-1;
    for(int i=0;i<=high;){
      if(arr[i]==0){
        swap(arr, low, i);
        low++;
        i++;
      }else if(arr[i]==1){
        i++;
      }else{
        swap(arr, high, i);
        high--;
      }
    }
  }
 private:
  static void swap(vector<int> &arr,int n1,int n2){
    int tmp=arr[n2];
    arr[n2]=arr[n1];
    arr[n1]=tmp;
    return;
  }
};

int main(int argc, char *argv[]) {
  vector<int> arr = {2, 0, 2, 1, 1};
  for (auto num : arr) {
    cout << num << " ";
  }
  cout << " =sort=> ";
  DutchFlag::sort(arr);
  for (auto num : arr) {
    cout << num << " ";
  }
  cout << endl;
}