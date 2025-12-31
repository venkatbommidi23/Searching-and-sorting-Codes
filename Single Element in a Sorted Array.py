#https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

class Solution(object):
    def singleNonDuplicate(self, nums):
        high=len(nums)-1

        # Case 1: Only one element in array
        if len(nums)==1:
            return nums[0]
        
        # Case 2: Single element is at the beginning
        # First element is not equal to second
        if nums[0]!=nums[1]:
            return nums[0]
        # Case 3: Single element is at the end
        # Last element is not equal to second last
        if nums[high]!=nums[high-1]:
            return nums[high]
           
        # We already checked index 0 and n-1
        low=1
        high=len(nums)-2
        while low<=high:
            mid=(low+high)//2

            # If mid element is not equal to both neighbors
            # ade single element
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]

            # If mid index is EVEN
            if mid%2==0:
                # Normally, even index element should match right neighbor
                #example:[1,1,2,2,3,4,4] here 1st 2 is at even index and next 2 is at odd this is correct,
                #so single element is on right.
                if nums[mid]==nums[mid+1]:
                    # Pattern is correct till mid
                    # Single element is on right side
                    low=mid+1
                else:
                    high=mid-1
            else:
                # Normally, odd index element should match left neighbor
                if nums[mid]==nums[mid-1]:
                    # Pattern is correct
                    # Single element is on right side
                    low=mid+1
                else:
                    high=mid-1
  
    #Time complexity-O(logn)
    #Space complexity-O(1)
