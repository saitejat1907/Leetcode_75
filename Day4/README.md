# Day 4: Longest Substring Without Repeating Characters

## Description

This project focuses on solving the "Longest Substring Without Repeating Characters" problem from LeetCode. The challenge is to find the length of the longest substring in a given string that does not contain repeating characters.

## Problem Statement

Check out the problem statement here: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

## Solution Approach

I implemented a sliding window approach to solve the problem, which efficiently tracks the longest substring without repeating characters.

### Approach: Sliding Window with Hash Set
- **Method:**
    - I utilized a hash set to keep track of the characters in the current substring.
    - Two pointers, `left` and `right`, represent the current window of characters. The `right` pointer expands the window by iterating through the string, while the `left` pointer contracts the window when a repeating character is found.
    - If the current character is already in the hash set, the `left` pointer is moved to the right until the duplicate character is removed from the set.
    - The maximum length of the substring is updated throughout the process.
    - **Time Complexity:** O(n), where `n` is the number of characters in the string. This approach efficiently finds the longest substring by leveraging the hash set for quick lookups.

## Code Explanation

- **Sliding Window Approach:** 
    - This method maintains a dynamic window that grows and shrinks based on the characters encountered. By using a hash set, we can quickly check for duplicates and ensure that the substring remains unique.

### Example Walkthrough
Given the input string `s = "abcabcbb"`, the sliding window approach will iterate through the string as follows:

| Iteration | `right` | Current Character | `char_set`            | Action/Explanation                                                                  | `max_length` |
|-----------|---------|-------------------|-----------------------|------------------------------------------------------------------------------------|---------------|
| 0         | 0       | 'a'               | {}                    | Add 'a' to `char_set`.                                                            | 1             |
| 1         | 1       | 'b'               | {'a'}                | Add 'b' to `char_set`.                                                            | 2             |
| 2         | 2       | 'c'               | {'a', 'b'}           | Add 'c' to `char_set`.                                                            | 3             |
| 3         | 3       | 'a'               | {'a', 'b', 'c'}      | 'a' is already in `char_set`. Shrink the window from the left.                   | 3             |
|           |         |                   | {'b', 'c'}           | Remove `s[left]` ('a'), increment `left` to 1.                                   |               |
|           |         |                   | {'b', 'c', 'a'}      | Add 'a' back to `char_set`.                                                       |               |
|           |         |                   | {'b', 'c', 'a'}      | Update `max_length` to 3.                                                          |               |
| 4         | 4       | 'b'               | {'b', 'c', 'a'}      | 'b' is already in `char_set`. Shrink the window from the left.                   | 3             |
|           |         |                   | {'c', 'a'}           | Remove `s[left]` ('b'), increment `left` to 2.                                   |               |
|           |         |                   | {'a', 'b'}           | Add 'b' back to `char_set`.                                                       |               |
|           |         |                   | {'a', 'b'}           | Update `max_length` to 3.                                                          |               |
| 5         | 5       | 'c'               | {'a', 'b'}           | 'c' is already in `char_set`. Shrink the window from the left.                   | 3             |
|           |         |                   | {'a'}                | Remove `s[left]` ('c'), increment `left` to 3.                                   |               |
|           |         |                   | {'a', 'b', 'c'}      | Add 'c' back to `char_set`.                                                       |               |
|           |         |                   | {'a', 'b', 'c'}      | Update `max_length` to 3.                                                          |               |
| 6         | 6       | 'b'               | {'a', 'b', 'c'}      | 'b' is already in `char_set`. Shrink the window from the left.                   | 3             |
|           |         |                   | {'a', 'c'}           | Remove `s[left]` ('b'), increment `left` to 4.                                   |               |
|           |         |                   | {'a', 'c', 'b'}      | Add 'b' back to `char_set`.                                                       |               |
|           |         |                   | {'a', 'c', 'b'}      | Update `max_length` to 3.                                                          |               |
| 7         | 7       | 'b'               | {'a', 'c', 'b'}      | 'b' is already in `char_set`. Shrink the window from the left.                   | 3             |
|           |         |                   | {'c'}                | Remove `s[left]` ('b'), increment `left` to 5.                                   |               |
|           |         |                   | {'c', 'b'}           | Add 'b' back to `char_set`.                                                       |               |
|           |         |                   | {'c', 'b'}           | Update `max_length` to 3.                                                          | 3             |

### Final Result
After iterating through the string, the maximum length of a substring without repeating characters is **3**, and the substrings that meet this length are "abc", "bca", or "cab".

## Contributions
Feel free to contribute to this project by submitting issues or pull requests.
