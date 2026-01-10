 #https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:
    def searchRange(self, nums, target):
        low=0
        high=len(nums)-1
        first_occurence=-1
        while(low<=high):
            mid=(low+high)//2
            if (target==nums[mid]):
                first_occurence=mid
                high=mid-1
            elif (target>nums[mid]):
                low=mid+1
            else:
                high=mid-1
        
        low=0
        high=len(nums)-1
        last_occurence=-1
        while (low<=high):
            mid=(low+high)//2
            if (target==nums[mid]):
                last_occurence=mid
                low=mid+1
            elif (target>nums[mid]):
                low=mid+1
            else:
                high=mid-1
        
        return first_occurence,last_occurence

        #Time complexity-O(logn)
        #Space Complexity-O(1) 
