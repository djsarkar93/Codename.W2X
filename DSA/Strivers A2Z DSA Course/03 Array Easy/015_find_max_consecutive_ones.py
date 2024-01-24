########################################################################################################################
# Count Maximum Consecutive One’s in the array
########################################################################################################################
# Problem Statement: 
# Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.
#
# Example 1:
# Input: arr = [1, 1, 0, 1, 1, 1]
# Output: 3
# Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.
# 
# Example 2:
# Input: arr = [1, 0, 1, 1, 0, 1]
# Output: 2
# Explanation: There are two consecutive 1's in the array.
########################################################################################################################



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def find_max_consecutive_ones(arr):
    n = len(arr)
    max_count = counter = 0
    for i in range(0, n):
        if arr[i] == 1:
            counter += 1
        else:
            counter = 0
        max_count = max(counter, max_count)
    return max_count
