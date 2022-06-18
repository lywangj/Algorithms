using namespace std;

#include <iostream>
#include <vector>

class Interval {
 public:
  int start = 0;
  int end = 0;

  Interval(int start, int end) {
    this->start = start;
    this->end = end;
  }
};

class IntervalsIntersection {
 public:
  static vector<Interval> merge(const vector<Interval> &arr1, const vector<Interval> &arr2) {
    vector<Interval> result;
    int p1=0;
    int p2=0;
    while(p1<arr1.size()&&p2<arr2.size()) {
      if((arr1[p1].start<=arr2[p2].start && arr1[p1].end>=arr2[p2].start) ||
        (arr2[p2].start<=arr1[p1].start && arr2[p2].end>=arr1[p1].start) ) {
        int start=max(arr1[p1].start,arr2[p2].start);
        int end=min(arr1[p1].end,arr2[p2].end);
        result.push_back({start,end});
      }
      if(arr1[p1].end<arr2[p2].end) {
        p1++;
      } else {
        p2++;
      }
    }
    return result;
  }
};

int main(int argc, char *argv[]) {
  vector<Interval> input1 = {{1, 3}, {5, 6}, {7, 9}};
  vector<Interval> input2 = {{2, 3}, {5, 7}};
  vector<Interval> result = IntervalsIntersection::merge(input1, input2);
  cout << "Intervals Intersection: ";
  for (auto interval : result) {
    cout << "[" << interval.start << "," << interval.end << "] ";
  }
  cout << endl;

  input1 = {{1, 3}, {5, 7}, {9, 12}};
  input2 = {{5, 10}};
  result = IntervalsIntersection::merge(input1, input2);
  cout << "Intervals Intersection: ";
  for (auto interval : result) {
    cout << "[" << interval.start << "," << interval.end << "] ";
  }
}
