########################################################################################################################
# Move all Zeros to the end of the array
########################################################################################################################
# Problem Statement: 
# You are given an array of integers, your task is to move all the zeros in the array to the end of the array 
# and move non-negative integers to the front by maintaining their order.
#
# Example 1:
# Input: arr = [1,0,2,3,0,4,0,1]
# Output: arr = [1,2,3,4,1,0,0,0]
# Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
#
# Example 2:
# Input: arr = [1,2,0,1,0,4,0]
# Output: arr = [1,2,1,4,0,0,0]
# Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
########################################################################################################################



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def move_zeroes(arr):
    n = len(arr)

    i = -1
    for j in range(0, n):
        if arr[j] == 0:
            i = j
            break
    else:
        return 
    
    for j in range(i+1, n):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
