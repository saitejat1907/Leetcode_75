# Day 1: [Best Time to Buy and Sell Stock]

## Description

This problem includes concepts related to arrays, time complexity, optimizing code which gives a better excitement as there is small trick in the problem

## Problem Statement

Checkout the problem statement here: [click here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=xi4ci4ig)

## Solution Approach

I made three attempts to solve the problem, refining my approach each time:

### First Attempt
- **Approach:** 
    - I started by finding the least number in the list.
    - Then, I calculated the difference with the upcoming highest number in the list.
- **Result:** This approach didn't work as expected due to incorrect selection of the least number.

### Second Attempt
- **Approach:**
    - I initially considered the first element as the minimum value.
    - I then calculated the difference between the first element and the greatest number in the remaining list.
- **Result:** Although this solved the problem, it resulted in high time complexity, leading to a time complexity error.

### Third Attempt (Final Solution)
- **Approach:**
    - I followed a linear approach where I treated the first element of the array as the minimum value.
    - For each subsequent number, I checked if it was larger than the current minimum value. If so, I calculated the profit and updated the maximum profit.
    - If a smaller value was found, I updated the minimum value and continued the iteration.
- **Result:** This approach optimized the time complexity and successfully solved the problem.


### Code Explanation:
- **min_price:** Tracks the lowest price encountered so far.
- **max_profit:** Tracks the maximum profit achieved by comparing the current price with the minimum price.
- **Algorithm:** The code iterates through the list of prices and dynamically calculates the profit while updating both the minimum price and maximum profit.


## Result
![Result](https://github.com/saitejat1907/Leetcode_75/blob/main/Day1/result.jpg)
