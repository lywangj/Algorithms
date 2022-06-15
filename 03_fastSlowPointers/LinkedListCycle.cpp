using namespace std;

#include <iostream>

class ListNode {
 public:
  int value = 0;
  ListNode *next;

  ListNode(int value) {
    this->value = value;
    next = nullptr;
  }
};

class LinkedListCycleStart {
 public:
  static ListNode *findCycleStart(ListNode *head) {
    /* setup one fast pointer & one slow pointer */
    ListNode* slow = head;
    ListNode* fast = head->next;

    /* moving two pointers forward 
      until they point to the same node due to cycle */
    while(slow!=fast){
      slow=slow->next;
      fast=fast->next->next;
    }

    /* count n, the number of nodes in cycle */
    fast=fast->next;
    int n=1;
    while(slow!=fast){
      fast=fast->next;
      n++;
    }

    /* move fast pointer nth-node ahead of slow pointer */
    slow = head;
    fast = head;
    for(int i=0;i<n;++i){
      fast=fast->next;
    }

    /* when slow pointer catch up fast pointer
      Their meeting point will be the start of the cycle. */
    while(slow!=fast){
      slow=slow->next;
      fast=fast->next;
    }
    head=slow;

    return head;
  }
};

int main(int argc, char *argv[]) {
  ListNode *head = new ListNode(1);
  head->next = new ListNode(2);
  head->next->next = new ListNode(3);
  head->next->next->next = new ListNode(4);
  head->next->next->next->next = new ListNode(5);
  head->next->next->next->next->next = new ListNode(6);

  head->next->next->next->next->next->next = head->next->next;
  cout << "LinkedList cycle start: " << LinkedListCycleStart::findCycleStart(head)->value << endl;

  head->next->next->next->next->next->next = head->next->next->next;
  cout << "LinkedList cycle start: " << LinkedListCycleStart::findCycleStart(head)->value << endl;

  head->next->next->next->next->next->next = head;
  cout << "LinkedList cycle start: " << LinkedListCycleStart::findCycleStart(head)->value << endl;
}
