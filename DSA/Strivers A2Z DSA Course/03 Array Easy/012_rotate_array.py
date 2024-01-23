########################################################################################################################
# Rotate array by K elements
########################################################################################################################
# Problem Statement: 
# Given an array of integers, rotate its elements by k elements either left or right.
#
# Example 1:
# Input: arr = [1,2,3,4,5,6,7], k = 2, right
# Output: arr = [6, 7, 1, 2, 3, 4, 5]
# Explanation: Array is rotated to right by 2 position.
# 
# Example 2:
# Input: arr = [3, 7, 8, 9, 10, 11], k = 3, left
# Output: arr = [9, 10, 11, 3, 7, 8]
# Explanation: Array is rotated to left by 3 position.
########################################################################################################################



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( 2n )
# Space Complexity: O( 1 )
########################################################################################################################
def rorate_array(arr, k, mode):
    n = len(arr)
    k = k % len(arr)
    bkp_arr = []

    if mode.upper() == 'LEFT':
        for i in range(0, k):
            bkp_arr.append(arr[i])

        for i in range(k, n):
            arr[i-k] = arr[i]
        
        j = 0
        for i in range(n-k, n):
            arr[i] = bkp_arr[j]
            j += 1
    
    elif mode.upper() == 'RIGHT':
        for i in range(n-k, n):
            bkp_arr.append(arr[i])
        
        for i in range(n-k-1, -1, -1):
            arr[i+k] = arr[i]
        
        for i in range(0, k):
            arr[i] = bkp_arr[i]



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( 2n )
# Space Complexity: O( 1 )
########################################################################################################################
def reverse(arr, start, end):
    while start <= end:
        arr[ start ], arr[ end ] = arr[ end ], arr[ start ]
        start += 1
        end -= 1

def rorate_array(arr, k, mode):
    n = len(arr)
    k = k % n

    if mode.upper() == 'LEFT':
        reverse(arr, start = 0, end = k-1)
        reverse(arr, start = k, end = n-1)
        reverse(arr, start = 0, end = n-1)
    
    elif mode.upper() == 'RIGHT':
        reverse(arr, start = 0, end = n-k-1)
        reverse(arr, start = n-k, end = n-1)
        reverse(arr, start = 0, end = n-1)
