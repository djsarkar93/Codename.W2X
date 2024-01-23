########################################################################################################################
# Linear Search
########################################################################################################################
# Problem Statement: 
# Given an array, and an element 'num' the task is to find if 'num' is present in the given array or not. 
# If present print the index of the element or print -1.
#
# Example 1:
# Input: arr = [1, 2, 3, 4, 5], num = 3
# Output: 2
# Explanation: 3 is present in the 2nd index
#
# Example 2:
# Input: arr = [5, 4, 3, 2, 1], num = 5
# Output: 0
# Explanation: 5 is present in the 0th index
########################################################################################################################



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( n )
# Space Complexity: O( 1 )
#
# Note:
# - To find the first occurrence, use: range(0, n)
# - To find the last  occurrence, use: range(n-1, -1, -1)
# - To find all occurrences, store the matched indexes in a list.
########################################################################################################################
def linear_search(arr, num):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == num:
            return i 
    return -1
