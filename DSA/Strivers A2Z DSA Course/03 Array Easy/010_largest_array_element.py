########################################################################################################################
# Largest array element
########################################################################################################################
# Problem Statement: 
# Given an array, we have to find the largest element in the array.
#
# Example 1:
# Input: arr = [2,5,1,3,0]
# Output: 5
# Explanation: 5 is the largest element in the array. 
#
# Example 2: 
# Input: arr = [8,10,5,7,9]
# Output: 10
# Explanation: 10 is the largest element in the array.
########################################################################################################################



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def largest_array_element(arr):
    largest = arr[0]
    n = len(arr)
    for i in range(1, n):
        largest = max(arr[i], largest)
    return largest
