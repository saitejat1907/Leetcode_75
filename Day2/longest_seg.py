# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # nums = sorted(set(nums))
#         # n = len(nums)
#         # length = 1
#         # diff = 0
#         # for i in range(n - 1):
#         #     diff = nums[i+1] - nums[i]
#         #     if(diff == 1):
#         #         length = length + 1
#         #         result[i] = a
#         #     else:
#         #         result[i] = length
#         #         length = 1
        
#         # return length

#     if not nums:
#       return 0  # Return 0 if array is empty

#     # Sort the array to handle sequences
#     nums = sorted(nums)
    
#     result = []
#     sequence_marker = 1  # Start with 1 for the first sequence

#     for i in range(1, len(nums)):
#         # Check the difference between consecutive elements
#         if nums[i] - nums[i - 1] == 1:
#             result.append(1)  # Store 1 for consecutive numbers
#         else:
#             result.append(sequence_marker)  # Store sequence_marker for non-consecutive numbers
#             sequence_marker += 1  # Increment marker for new sequences
    
#     # Include the last marker
#     result.append(sequence_marker)

#     # Count the occurrences of each sequence marker
#     count_occurrences = Counter(result)

#     # Find the most frequent sequence marker and return its frequency
#     most_frequent_count = max(count_occurrences.values())
    
#     return most_frequent_count

# Second Approach

# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0  # Return 0 if the list is empty

#         # Sort the array to handle sequences
#         nums = sorted(set(nums))
        
#         result = []
#         sequence_marker = 1  # Start with 1 for the first sequence

#         for i in range(1, len(nums)):
#             # Check the difference between consecutive elements
#             if nums[i] - nums[i - 1] == 1:
#                 result.append(1)  # Store 1 for consecutive numbers
#             else:
#                 result.append(sequence_marker)  # Store sequence_marker for non-consecutive numbers
#                 sequence_marker += 1  # Increment marker for new sequences
        
#         # Include the last marker
#         result.append(sequence_marker)

#         # Count the occurrences of each sequence marker
#         count_occurrences = Counter(result)

#         # Find the most frequent sequence marker and return its frequency
#         most_frequent_count = max(count_occurrences.values())
        
#         return most_frequent_count

# Third Approach

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Use a set to remove duplicates and allow O(1) lookups
        nums_set = set(nums)
        longest_sequence = 0

        # Iterate over the numbers
        for num in nums_set:
            # Only start a new sequence if num-1 is not in the set
            if num - 1 not in nums_set:
                current_num = num
                current_sequence = 1

                # Count the length of the consecutive sequence
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_sequence += 1

                # Update the longest sequence found
                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

# Example usage:
sol = Solution()
nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print(sol.longestConsecutive(nums))  # Expected Output: 7
