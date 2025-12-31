#https://leetcode.com/problems/find-peak-element/description/
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1

        low=1
        high=len(nums)-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            # If slope is increasing (left < mid),
            # then peak must be on the right side
            if nums[mid-1]<nums[mid]:
                low=mid+1
            # Slope is decreasing, peak is on the left side
            else:
                high=mid-1
        #“We use binary search by observing the slope of the array. If the slope is increasing, 
        #a peak lies on the right; if decreasing, it lies on the left. This gives an O(log n) solution.”

        #Time-O(logn)
        #Space-O(1)
