# https://www.geeksforgeeks.org/problems/implement-lower-bound/1
#Lower Bound
# Given a sorted array arr[] and a number target, the task is to find the lower bound of the target in this given array.
# The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.
# Note: If all the elements in the given array are smaller than the target, the lower bound will be the length of the array. 

# Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 11
# Output: 4
# Explanation: 4 is the smallest index in arr[] where element (arr[4] = 11) is greater than or equal to 11.

class Solution:
    def lowerBound(self, arr, target):
        lower_bound=len(arr)
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2  #low + (high-low)//2
            if arr[mid]>=target:
                lower_bound=mid
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            
        return lower_bound
        
        #Time Complexity-O(logn)
        #Space Complexity-0(1)

 
#https://www.geeksforgeeks.org/problems/implement-upper-bound/1
# Upper Bound -Given a sorted array arr[] and a number target, the task is to find the upper bound of the target in this given array.
# The upper bound of a number is defined as the smallest index in the sorted array where the element is greater than the given number.
# Note: If all the elements in the given array are smaller than or equal to the target, the upper bound will be the length of the array

# Input: arr[] = [2, 3, 7, 10, 11, 11, 25], target = 11
# Output: 6
# Explanation: 6 is the smallest index in arr[], at which element (arr[6] = 25) is larger than 11
class Solution:
    def lowerBound(self, arr, target):
        lower_bound=len(arr)
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2  #low + (high-low)//2
            if arr[mid]>=target:
                lower_bound=mid
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            
        return lower_bound
        
        #Time Complexity-O(logn)
        #Space Complexity-0(1)
            
            
        
