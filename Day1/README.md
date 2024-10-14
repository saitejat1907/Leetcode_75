# Day 2: Longest Consecutive Sequence

## Description

This project focuses on solving the "Longest Consecutive Sequence" problem. The challenge involves finding the longest sequence of consecutive integers in an unsorted array, optimizing the solution using set operations.

## Problem Statement

Check out the problem statement here: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=xi4ci4ig)

## Solution Approach

I made two attempts to solve the problem, refining my approach each time:

### First Attempt
- **Approach:** 
    - I sorted the array and stored `1` for consecutive numbers. If the sequence broke, I stored `2` for the next sequence, and so on.
    - In the result array, I counted the occurrences of each number and returned the highest count.
  
### Second Attempt (Final Solution)
- **Approach:**
    - I used a set to handle duplicates and check for the presence of consecutive numbers without sorting the array.
    - For each number, I checked if the previous number wasn't present in the set. If true, I started counting the sequence length from that number.
    - I then iterated to find the length of that consecutive sequence, updating the maximum length found.
  
## Code Explanation
- **Set Usage:** A set is used to eliminate duplicates and facilitate efficient membership testing.
- **Algorithm:** The code iterates through the unique numbers, checking for the existence of consecutive integers and dynamically calculating the length of the longest sequence.

## Result
![Result](https://github.com/saitejat1907/Leetcode_75/blob/main/Day2/image.png)

## Contributions

Feel free to contribute to this project by submitting issues or pull requests.

