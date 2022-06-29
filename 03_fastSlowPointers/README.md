### Start of LinkedList Cycle

Given the **head** of a **LinkedList** containing a cycle, 

try to find the starting node of the cycle.

- LinkedList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3
- starting node of cycle: 3

Task:
- Using two pointers, one moving faster than the other, to solve this problem without any extra space

Time complexity: O(n)
- N as the length of the given LinkedList

Space complexity: O(1)
- no extra space

Constraints:
- 0 <= n, Number of ListNodes <= 1000
- ListNode(i)->next == ListNode(i), i < j < n-1
- only one unique cycle in LinkedList

<img src="../images/2022-06-15_002247.png" height="280">
<a class="return" href="../README.md" style="text-align:right;"> 《BACK》 </a>
