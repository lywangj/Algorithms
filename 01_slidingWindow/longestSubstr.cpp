using namespace std;

#include <iostream>
#include <string>
#include <vector>

class NoRepeatSubstring {
 public:
  static int findLength(const string& str) {
    int maxLength = 0;
    vector<int> dict(128,-1);
    int startSt=0;
    for(int endSt=0;endSt<str.length();++endSt){
      if(dict[str[endSt]]>-1){
        startSt=dict[str[endSt]]+1;
      }
      dict[str[endSt]]=endSt;
      maxLength=max(maxLength,endSt-startSt+1);
    }
    return maxLength;
  }
};

int main(int argc, char* argv[]) {
  cout << "Length of the longest substring: " << NoRepeatSubstring::findLength("aabccbb") << endl;
  cout << "Length of the longest substring: " << NoRepeatSubstring::findLength("abbbb") << endl;
  cout << "Length of the longest substring: " << NoRepeatSubstring::findLength("abccde") << endl;
  cout << "Length of the longest substring: " << NoRepeatSubstring::findLength("bbabcabcdd") << endl;
}
