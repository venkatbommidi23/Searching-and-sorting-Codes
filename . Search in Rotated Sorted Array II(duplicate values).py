#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#Search in Rotated Sorted Array II

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid]==nums[high]: #If all three are same we cannot say which side is sorted so we will shrink the array
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:       # left is sorted
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:                 #Right is sorted
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False

       #Time Complexity:
       #O(logn)-best/average case
       #O(n)-Worst case because 
       #Because duplicates can prevent us from identifying the sorted half, forcing linear shrink
       #“When all elements are duplicates and the target is absent, binary search cannot determine the sorted half and is forced to shrink the range one element at a time, leading to linear time.
       #Space-O(1)
            
                    
        
