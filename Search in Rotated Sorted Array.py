#https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            
            # Check if LEFT half is sorted
            elif nums[low]<=nums[mid]:

                # Target left sorted part lo unte
                if nums[low]<=target<nums[mid]:
                    # left side ki move avvali
                    high=mid-1
                else:
                    low=mid+1  # target right side lo undi

            # Else RIGHT half is sorted
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1

        #Time complexity-O(logn)  # Array ni prathi step lo half chestunnam kabatti
        #space complexity-O(1)
        
