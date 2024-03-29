### Reverse a Sub-list

Given a linked **list** with nodes marked order numbers, revere sub-list from 'p'th node to 'q'th node, and keep the other nodes in the same order.

- start to revere, p = 2
- end to reverse, q = 4
- input-list : 1 -> 2 -> 3 -> 4 -> 5 -> null
- output-list : 1 -> 4 -> 3 -> 2 -> 5 -> null

**Task**:
- try to find an efficient way to implemnt in-place revere sub-list without extra space.

**Exercise**: [reversedSubList.py](reversedSubList.py)

Time complexity: O(n), N as the length of **list**

Space complexity: O(1), constant space

Constraints:
- 1 <= list.length <= 1000
- list[i] = i

<img src="../images/2022-06-26_002007.png" height="290">
<a class="return" href="../README.md" style="text-align:right;"> 《BACK》 </a>
