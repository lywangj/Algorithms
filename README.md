## Algorithms
Learning plan for top 16 algorithms and data structures. The goal is to develop an understanding of the underlying pattern and be able to solve a specific category of problems.

<a class="d-block width-auto" href="#quoting-text">Link</a>

### Chapter 01. Sliding Window

A sliding window pattern will solve this problem in an more effecient way, **time complexity O(n)** - n as the size of the given array.
Compared with this, a basic brute force solution will be with time complexity O(n*k) - k as the number of the targeted elements.

- Exercise: Longest Substring without Repeating Characters
- Input string = "bbabcabcdd"
- Output: 4
- Explain: the longest substring w/o repeating characters is "abcd", and the length is 4.

<img src="images/2022-06-06_002359.png" height="260">

#
### Chapter 02. Two Pointers
<h2 id="quoting-text"> "Chapter 02. Two Pointers" </h2>
If input array is sorted, an efficient way, **time complexity O(n)**, would be to with one pointer in the beginning and another pointer at the end. At every step, pointers iterate through the remaining elements, until these two pointers pointing to the same elements.

Compared with this, a basic brute force solution will be with time complexity O(n\*n), and a heapsort solution will be with O(n*logn).

- Exercise: Dutch National Flag Problem
- Input array =  [2, 0, 1, 1, 1]
- Output array = [0, 1, 1, 1, 2]
- Explain: incrementally sort an array containing only three objects (labled as 0, 1 & 2)

<img src="images/2022-06-11_001942.png" height="260">

#
### Chapter 03. Fast & Slow Pointers

Setting two pointers with different move speed would be **time complexity O(n)** and with space complexity O(1), no extra space. 

- Exercise: Start of LinkedList Cycle
- LinkedList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3
- starting node of cycle: 3
- Explain: Node 3 is start of cycle (3 -> 4 -> 5 -> 6 -> 3)

<img src="images/2022-06-15_002247.png" height="280">

#
### Chapter 04. Merge Intervals
