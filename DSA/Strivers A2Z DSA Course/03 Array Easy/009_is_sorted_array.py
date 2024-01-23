########################################################################################################################
# Is sorted array
########################################################################################################################
# Problem Statement: 
# Given an array of size n, write a program to check if the given array is sorted in ascending order or not. 
# If the array is sorted then return True, Else return False.
#
# Example 1:
# Input: arr = [1, 2, 3, 4, 5]
# Output: True.
# Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values.
########################################################################################################################



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def is_sorted_array(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            return False
    return True
