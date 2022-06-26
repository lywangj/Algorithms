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

class ReverseSubList {
 public:
  static ListNode *reverse(ListNode *head, int p, int q) {
    if (p == q) {
      return head;
    }

    // Skipping 'p-1' nodes, move current pointer to 'p'th node
    ListNode *curr = head, *prev = nullptr;
    for (int i=0; curr!=nullptr && i<p-1; ++i) {
      prev=curr;
      curr=curr->next;
    }

    // set a mark pointing to the node at index 'p-1'
    ListNode *lastNodeOfFirst=prev;

    // set a mark pointing to the node at index 'p' 
    // that will be the last node of reversed sub list.
    ListNode *lastNodeOfSub=curr;

    // reverse nodes between 'p' and 'q'
    ListNode *next=nullptr;
    for (int i=0; curr!=nullptr && i<q-p+1; i++) {
      next=curr->next;
      curr->next=prev;
      prev=curr;
      curr=next;
    }

    // connect first part to reversed sub list
    if (lastNodeOfFirst!=nullptr) {
      // 'prev' is now the first node of the sub-list
      lastNodeOfFirst->next=prev;  
    } else {
      head=previous;
    }

    // connect with the last part
    // 'curr' is now the first node of the last part
    lastNodeOfSub->next=curr;

    return head;
  }
};

int main(int argc, char *argv[]) {
  ListNode *head = new ListNode(1);
  head->next = new ListNode(2);
  head->next->next = new ListNode(3);
  head->next->next->next = new ListNode(4);
  head->next->next->next->next = new ListNode(5);

  ListNode *result = ReverseSubList::reverse(head, 2, 4);
  cout << "Nodes of the reversed LinkedList are: ";
  while (result != nullptr) {
    cout << result->value << " ";
    result = result->next;
  }
}