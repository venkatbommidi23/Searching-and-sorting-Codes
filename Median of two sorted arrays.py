#https://www.naukri.com/code360/problems/median-of-two-sorted-arrays_985294?leftPanelTabValue=PROBLEM

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n))
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.


def median(nums1: int, nums2: int) -> float:
        #Brute Force 
        #Time - O(m+n)
        #SPace-O(m+n)
        arr=[]
        i=0
        j=0
        m=len(nums1)
        n=len(nums2)
        while i< m and j < n:
            if nums1[i] < nums2[j] :
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        
        while i < m:
            arr.append(nums1[i])
            i+=1
        
        while j < n:
            arr.append(nums2[j])
            j+=1
        
        l=len(arr)

        if l%2==0:
            return (arr[l//2]+arr[(l//2)-1])/2.0
        else:
            return float(arr[l//2])
