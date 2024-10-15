# Day 3: Two Sum

## Description

This project focuses on solving the "Two Sum" problem from LeetCode. The challenge is to find two numbers in an array that add up to a specific target and return their indices.

## Problem Statement

Check out the problem statement here: [Two Sum](https://leetcode.com/problems/two-sum/description/)

## Solution Approach

I implemented two approaches to solve the problem. Both methods return the correct result, but differ in their efficiency.

### First Attempt: Brute Force
- **Approach:**
    - I used two nested loops. For each element in the array, the outer loop holds the element constant, while the inner loop iterates over the remaining elements and checks if their sum equals the target.
    - If a pair is found, their indices are returned immediately.
    - **Time Complexity:** O(n²), where `n` is the number of elements in the array.

### Second Attempt (Final Solution): Hash Map
- **Approach:**
    - I used a hash map (or dictionary) to store the elements of the array and their corresponding indices.
    - For each element, I computed the complement (i.e., `target - nums[i]`) and checked if the complement exists in the hash map.
    - If the complement exists and is not the current element, their indices are returned.
    - **Time Complexity:** O(n), where `n` is the number of elements in the array. This method is much faster as it reduces the time complexity using a hash table for efficient lookup.

## Code Explanation

- **First Approach (Brute Force):** Two for-loops iterate through the array, adding pairs of elements to find a match for the target.
- **Second Approach (Hash Table):** A single pass through the array, using a hash table for complement lookup and efficient retrieval of the result.

### Hash Map Example
Given an array `nums = [2, 7, 11, 15]` and a target of `9`, the hash map stores elements and their indices like so:
```python
{2: 0, 7: 1, 11: 2, 15: 3}
```

The complement of `2` is `7`, which exists in the hash map, so the solution is `[0, 1]`.

## Result
Both methods produce the correct result, but the second approach is much faster for larger inputs.

## Contributions
Feel free to contribute to this project by submitting issues or pull requests.
