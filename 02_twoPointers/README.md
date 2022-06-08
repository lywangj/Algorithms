### Longest Substring without Repeating Characters


<!-- 
Allow user to input a string, which consists of English letters, digits, symbols and spaces.

find the length of the longest substring without repeating characters

- Input string = "bbabcabcdd"
- Output: 4
- explain: the longest substring w/o repeating characters is "abcd", and the length is 4.

Task:
- Following sliding window pattern, to solve this problem with TC O(n)
- instead of Hashmap, an array can be a faster way to store each characters

Time complexity: O(n)
- n as the length of input string 

Space complexity: O(n)
- n as the length of dictionary (storing max. 128 types of characters)

Constraints:
- 0 <= string.length <= 10000 -->
