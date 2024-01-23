########################################################################################################################
# Second largest & smallest array element
########################################################################################################################
# Problem Statement: 
# Given an array, find the second largest & smallest elements in the array. 
# Print ‘-1’ in the event that either of them doesn’t exist.
#
# Example 1:
# Input: [1,2,4,7,7,5]
# Output: Second Largest : 5
# 	      Second Smallest: 2
# Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2
# 
# Example 2:
# Input: [1]
# Output: Second Largest : -1
# 	      Second Smallest: -1
# Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. 
#              There is no second largest or second smallest element present.
########################################################################################################################



########################################################################################################################
# Brute Force solution
#
# Time Complexity : O( n log n ) + O( 1 )
# Space Complexity: O( 1 )
#
# Note:
# - If array has no duplicates, return arr[1] as 2nd smallest & arr[-2] as 2nd largest.
########################################################################################################################
def find_second_min_max(arr):
    arr.sort()
    n = len(arr)
    
    smallest = arr[0]
    for i in range(1, n):
        if arr[i] > smallest:
            print(f'Second Smallest: {arr[i]}')
            break
    else:
        print('Second Smallest: -1')
    
    largest = arr[n-1]
    for i in range(n-1, -1, -1):
        if arr[i] < largest:
            print(f'Second Largest: {arr[i]}')
            break
    else:
        print('Second Largest: -1')



########################################################################################################################
# Better solution
#
# Time Complexity : O( 2n )
# Space Complexity: O( 1 )
########################################################################################################################
def find_second_min_max(arr):
    n = len(arr)

    smallest = largest = arr[0]
    for i in range(1, n):
        smallest = min(arr[i], smallest)
        largest = max(arr[i], largest)
    
    second_smallest = float('inf')
    second_largest = float('-inf')
    for i in range(0, n):
        if arr[i] != smallest:
            second_smallest = min(arr[i], second_smallest)
        if arr[i] != largest:
            second_largest = max(arr[i], second_largest)
    
    print(f"Second Smallest: {second_smallest if second_smallest != float('inf') else -1}")
    print(f"Second Largest: {second_largest if second_largest != float('-inf') else -1}")



########################################################################################################################
# Optimal solution
#
# Time Complexity : O( n )
# Space Complexity: O( 1 )
########################################################################################################################
def find_second_min_max(arr):
    n = len(arr)

    second_smallest = float('inf')
    smallest = arr[0]

    second_largest = float('-inf')
    largest = arr[0]

    for i in range(1, n):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] > smallest and arr[i] < second_smallest:
            second_smallest = arr[i]
        
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest:
            second_largest = arr[i]
    
    print(f"Second Smallest: {second_smallest if second_smallest != float('inf') else -1}")
    print(f"Second Largest: {second_largest if second_largest != float('-inf') else -1}")
