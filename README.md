<h2 id="top"> Algorithms </h2>
Learning plan for top 16 algorithms and data structures. The goal is to develop an understanding of the underlying pattern and be able to solve a specific category of problems.

<p></p>

<a class="outlines" href="#sliding-windows">______ 01. Sliding Window</a>

<a class="outlines" href="#two-pointers">______ 02. Two Pointers</a>

<a class="outlines" href="#fast-slow-pointers">______ 03. Fast & Slow Pointers</a>

<a class="outlines" href="#merge-intervals">______ 04. Merge Intervals</a>

<a class="outlines" href="#cyclic-sort">______ 05. Cyclic Sort</a>

<p></p>

#
<h3 id="sliding-windows"> Chapter 01. Sliding Window </h3>
A sliding window pattern will solve this problem in an more effecient way, **time complexity O(n)** - n as the size of the given array.
Compared with this, a basic brute force solution will be with time complexity O(n*k) - k as the number of the targeted elements.

- Exercise: [Longest Substring without Repeating Characters](01_slidingWindow/)
- Input string = "bbabcabcdd"
- Output: 4
- Explain: the longest substring w/o repeating characters is "abcd", and the length is 4.

<img src="images/2022-06-06_002359.png" height="260">
<a class="return" href="#top" style="text-align:right;"> 《TOP》 </a>

#
<h3 id="two-pointers"> Chapter 02. Two Pointers </h3>
If input array is sorted, an efficient way, **time complexity O(n)**, would be to with one pointer in the beginning and another pointer at the end. At every step, pointers iterate through the remaining elements, until these two pointers pointing to the same elements.

Compared with this, a basic brute force solution will be with time complexity O(n\*n), and a heapsort solution will be with O(n*logn).

- Exercise: Dutch National Flag Problem
- Input array =  [2, 0, 1, 1, 1]
- Output array = [0, 1, 1, 1, 2]
- Explain: incrementally sort an array containing only three objects (labled as 0, 1 & 2)

<img src="images/2022-06-11_001942.png" height="260">
<a class="return" href="#top"> 《TOP》 </a>

#
<h3 id="fast-slow-pointers"> Chapter 03. Fast & Slow Pointers </h3>
Setting two pointers with different move speed would be **time complexity O(n)** and with space complexity O(1), no extra space. 

- Exercise: Start of LinkedList Cycle
- LinkedList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3
- starting node of cycle: 3
- Explain: Node 3 is start of cycle (3 -> 4 -> 5 -> 6 -> 3)

<img src="images/2022-06-15_002247.png" height="280">
<a class="return" href="#top"> 《TOP》 </a>

#
<h3 id="merge-intervals"> Chapter 04. Merge Intervals </h3>
This would be an effecient way to deal with overlapping intervals with **time complexity O(n)** and space complexity O(1), no extra space.

- Exercise: Intervals Intersection
- arr1 = [1, 3], [5, 6], [7, 9]
- arr2 = [2, 3], [5, 7]
- output : [2, 3], [5, 6], [7, 7]

<img src="images/2022-06-19_002229.png" height="360">
<a class="return" href="#top"> 《TOP》 </a>

#
<h3 id="cyclic-sort"> Chapter 05. Cyclic Sort </h3>

<a class="return" href="#top"> 《TOP》 </a>
