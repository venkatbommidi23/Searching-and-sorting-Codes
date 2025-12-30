#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1869660215/
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        
        # Initialize minimum element as infinity
        MIN_ELEMENT = float('inf')

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2

            # Case 1: If the current subarray is already sorted
            # nums[low] <= nums[high] means no rotation in this range
            # So minimum will be at nums[low]
            if nums[low] <= nums[high]:
                MIN_ELEMENT = min(MIN_ELEMENT, nums[low])
                break   # further search not needed

            # Case 2: Left half is sorted
            # nums[low] <= nums[mid] means left side sorted
            if nums[low] <= nums[mid]:
                # Left half sorted ayindi, so min could be nums[low]
                MIN_ELEMENT = min(MIN_ELEMENT, nums[low])
                # Discard left half and move to right half
                low = mid + 1

            # Case 3: Right half is sorted (or left is unsorted)
            else:
                # Mid itself could be the minimum
                MIN_ELEMENT = min(MIN_ELEMENT, nums[mid])
                # Discard right half
                high = mid - 1

        return MIN_ELEMENT

#Time Complexity-O(logn)
#Space-O(1)
