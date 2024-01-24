########################################################################################################################
# Remove Duplicates in-place from Sorted Array
########################################################################################################################
# Problem Statement: 
# Remove duplicate numbers from a sorted array, keeping the order the same. 
# After removing duplicates, the first part of the array should show the result, and the length of this part (k) should be returned. 
# The rest of the array's content doesn't matter.
#
# Example 1: 
# Input: arr = [1,1,2,2,2,3,3]
# Output: arr = [1,2,3,_,_,_,_]
# Explanation: Total number of unique elements are 3, i.e. [1,2,3]. Therefore return 3 after assigning [1,2,3] in the beginning of the array.
# 
# Example 2: 
# Input: arr = [1,1,1,2,2,3,3,3,3,4,4]
# Output: arr = [1,2,3,4,_,_,_,_,_,_,_]
# Explanation: Total number of unique elements are 4, i.e. [1,2,3,4]. Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.
########################################################################################################################



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def remove_duplicates(arr):
    n = len(arr)

    if n == 0:
        return 0

    i = 0
    for j in range(1, n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    
    return i+1
