### Number Range

Given an array of numbers in ascending order, find the beginning and ending position of a given number, **key**. 

If **key** is not present in **arr**, then return [-1,-1].

Example1:
- arr = [4, 6, 6, 6, 9], key = 6
- Output: [1, 3]

Example2:
- arr = [1, 3, 8, 10, 15], key = 12
- Output: [-1, -1]

**Task**: With binary search method to design an effeceint solution

**Exercise**: [numberRange.py](numberRange.py)

Time complexity: O(logn), n as the length of **arr**

Space complexity: O(1), no extra space

Constraints:
- 1 <= len(**arr**) <= 100
- 1 <= arr[i]<= 100

<a class="return" href="../README.md" style="text-align:right;"> 《BACK》 </a>
